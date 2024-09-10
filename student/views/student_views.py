from django.shortcuts import render, redirect
from django.contrib import messages
from student.models.student import Student
from user.forms.user_forms import UserForm
from base.forms.formsAdr import AddressForm
from student.forms.formsStud import StudentForms
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='auth:login')
def index(request):
    search_field = request.GET.get('search')
    if search_field:
        students = Student.objects.filter(first_name__icontains=search_field ) | Student.objects.filter(last_name__icontains=search_field)
        context = {'students': students,
                   'search_field': search_field,
               }
    else:
        students = Student.objects.all()
        students_number = students.count()
        context = {'students': students,
                   'students_number': students_number,
               }
    return render(request, "student/index.html", context)

@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        student_form = StudentForms(request.POST)
        address_form = AddressForm(request.POST)
        user_form = UserForm(request.POST)

        if student_form.is_valid() and address_form.is_valid() and user_form:
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            address = address_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.address = address
            student.save()
            messages.success(request, "Eleve ajoute.")
            return redirect('student:index')
        else: 

            student_form = StudentForms()
            address_form = AddressForm()
            user_form = UserForm()

            messages.error(request, "Eleve non enregistre")
            #return render(request, "student/add_student.html" )
    
    student_form = StudentForms()
    address_form = AddressForm()
    user_form = UserForm()
    context = {'student_form': student_form,
               'address_form': address_form,
               'user_form': user_form, 
               'title': 'Ajouter  un éleve'
               }
    return render(request, "student/form.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    student = Student.objects.get(id=id)
    context = {'title': 'Modifier un élève'}
    if request.method == 'POST':
        student_form = StudentForms(request.POST, instance=student)
        address_form = AddressForm(request.POST, initial=student.address if student else None)
        user_form = UserForm(request.POST, instance=student.user if student else None)
        if student_form.is_valid() and address_form.is_valid() and user_form:
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            address = address_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.address = address
            student.save()
            messages.success(request, "Eleve modifié.")
            return redirect('student:index')
    else:
        student_form = StudentForms(instance=student)
    
    
    address_form = AddressForm(instance=student.address if student else None)
    user_form = UserForm(instance=student.user if student else None)    
    student_form = StudentForms(instance=student)
    context = {'student_form': student_form,
               'address_form': address_form,
               'user_form': user_form, 
               }
    return render(request, "student/form.html", context, )

@login_required(login_url='auth:login')
def delete(request, id): 
    student = Student.objects.get(id=id)
    student.delete()
    messages.warning(request, "Eleve supprime.")
    return redirect('student:index')
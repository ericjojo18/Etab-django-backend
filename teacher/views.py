from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.models.teacher import Teacher
from teacher.forms import  TeacherForms
from base.forms.formsAdr import AddressForm
from user.forms.user_forms import UserForm


# Create your views here.
@login_required(login_url='auth:login')
def index(request):
    
    search_field = request.GET.get('search')
    if search_field :
        teachers = Teacher.objects.filter(first_name__icontains=search_field) | Teacher.objects.filter(last_name__icontains=search_field)
        context = {
            'teachers': teachers,
            'search_field': search_field,
        }
    else:
        teachers = Teacher.objects.all()
        total_teachers = teachers.count()
        context = {
            'teachers': teachers,
            'total_teachers': total_teachers,

        }
    
    # teachers = Teacher.objects.all()
    # context = {'teachers': teachers}
    return render(request, "teacher/index.html", context)

@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        teacher_form = TeacherForms(request.POST)
        address_form = AddressForm(request.POST)
        user_form = UserForm(request.POST)
        
        if teacher_form.is_valid() and address_form.is_valid() and user_form:
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user.role.add(*user_form.cleaned_data.get('role'))
            
            address = address_form.save()
            
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.address = address
            teacher.save()
            # print(teacher)
            messages.success(request, "Professeur ajoute avec succes.")
            return redirect('teacher:index')
        else:
            teacher_form = TeacherForms()
            address_form = AddressForm()
            user_form = UserForm()
            messages.error(request, "Professeur non enregistre")
    
    teacher_form = TeacherForms()
    address_form = AddressForm()
    user_form = UserForm()
    content = {'teacher_form': teacher_form, 
                'address_form': address_form,
                'user_form': user_form, 
                'title': 'Ajouter un professeur'}
    return render(request,"teacher/form.html", content)

@login_required(login_url='auth:login')
def update(request, id):
    teacher = Teacher.objects.get(id=id)
    # print(teacher.id)
    context = {'title': 'Modifier un professeur'}
    
    if request.method == "POST":
        teacher_form = TeacherForms(request.POST, instance=teacher)
        address_form = AddressForm(request.POST, instance=teacher.address if teacher else None)
        user_form = UserForm(request.POST, instance=teacher.user if teacher else None)
        if teacher_form.is_valid() and address_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user.role.set(user_form.cleaned_data.get('role'))
            address = address_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.address = address
            teacher_form.save()
            messages.success(request, "Professeur modifie avec succes.")
            #print("Sauvegarde avec succes")
            return redirect('teacher:index')
        else:
            teacher_form = TeacherForms(instance=teacher)
            # address_form = AddressForm(instance=teacher.address if teacher else None)
            # user_form = UserForm(instance=teacher.user if teacher else None)
    
    teacher_form = TeacherForms(instance=teacher)
    address_form = AddressForm(instance=teacher.address if teacher else None)
    user_form = UserForm(instance=teacher.user if teacher else None)
    context = {
        'teacher_form': teacher_form,
        'address_form': address_form,
        'user_form': user_form,
        'title': 'Modifier un professeur'
    }
    # context["teacher_form"] = teacher_form
    return render(request, "teacher/form.html", context)

@login_required(login_url='auth:login')
def delete(request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        messages.success(request, "Professeur supprime avec succes.")
        return redirect('teacher:index')
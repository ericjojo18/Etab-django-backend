from django.shortcuts import render, redirect
from .forms import StudentForm, StudentForms
from .models import Student

# Create your views here.


def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, "student/index.html", context)

def add(request):
    
    if request.method == 'POST':
        student_form = StudentForms(request.POST)
        if student_form.is_valid():
            #Student.objects.create(**student_form.cleaned_data)
            print(student_form.cleaned_data)
            student_form.save()
            return redirect('student:index')
        else: 
            student_form = StudentForms()
            #return render(request, "student/add_student.html" )
    
    student_form = StudentForms()
    context = {'student_form': student_form,
               'title': 'Ajouter  un éleve'
               }
    return render(request, "student/form.html", context )

def update(request, id): 
    
    student = Student.objects.get(id=id)
    context = {'title': 'Modifier un élève'}
    if request.method == 'POST':
        student_form = StudentForms(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student:index')
    else:
        student_form = StudentForms(instance=student)
        
    student_form = StudentForms(instance=student)
    context ["student_form"] = student_form
    return render(request, "student/form.html", context, )


def delete(request, id):
        student = Student.objects.get(id=id)
        student .delete()
        return redirect('student:index')
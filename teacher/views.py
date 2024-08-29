from django.shortcuts import render, redirect
from .forms import  TeacherForms
from .models import Teacher


# Create your views here.

def index(request):
    
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, "teacher/index.html", context)

def add(request):
    
    if request.method == 'POST':
        teacher_form = TeacherForms(request.POST)
        if teacher_form.is_valid():
            #Teacher.objects.create(**teacher_form.cleaned_data)
            #print(teacher_form.cleaned_data)
            teacher_form.save()
            return redirect('teacher:index')
        else:
            teacher_form = TeacherForms()
    
    teacher_form = TeacherForms()
    content = {'teacher_form': teacher_form, 'title': 'Ajouter un professeur'}
    return render(request,"teacher/form.html", content)

def update(request, id):
    teacher = Teacher.objects.get(id=id)
    print(teacher.id)
    context = {'title': 'Modifier un professeur'}
    
    if request.method == "POST":
        teacher_form = TeacherForms(request.POST, instance=teacher)
        print(request.POST)
        if teacher_form.is_valid():
            print(teacher_form)
            user = teacher_form.cleaned_data
            print(user)
            teacher_form.save()
            print("Sauvegarde avec succes")
            return redirect('teacher:index')
    else:
        teacher_form = TeacherForms(instance=teacher)
    
    context["teacher_form"] = teacher_form
    return render(request, "teacher/form.html", context)


def delete(request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return redirect('teacher:index')
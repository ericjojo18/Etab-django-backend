# from django.shortcuts import render, redirect
# from django.contrib import messages
# from student.forms.formsStud import StudentForms
# from student.forms.FormsAbs import AbsenceForm
# from student.models.student import Student
# from student.models.absence import Absence
# from student.models.studentcards import StudentCards
# from django.contrib.auth.decorators import login_required


# # Create your views here.

# @login_required(login_url='auth:login')
# def index(request):
#     students = Student.objects.all()
#     absences = Absence.objects.all()
    
#     context = {'students': students,
#                'absences': absences
#                }
#     return render(request, "student/index.html", context)

# @login_required(login_url='auth:login')
# def add(request):
    
#     if request.method == 'POST':
#         student_form = StudentForms(request.POST)
#         print(0)
#         if student_form.is_valid():
#             print(2)
#             #Student.objects.create(**student_form.cleaned_data)
#             print(student_form.cleaned_data)
            
#             student_form.save()
#             messages.success(request, "Eleve ajoute.")
#             return redirect('student:index')
#         else: 
#             print(7)
#             student_form = StudentForms()
#             print(student_form.errors)
#             messages.error(request, "Eleve non")
#             #return render(request, "student/add_student.html" )
    
#     student_form = StudentForms()
#     context = {'student_form': student_form,
#                'title': 'Ajouter  un éleve'
#                }
#     return render(request, "student/form.html", context )

# @login_required(login_url='auth:login')
# def update(request, id): 
    
#     student = Student.objects.get(id=id)
#     context = {'title': 'Modifier un élève'}
#     if request.method == 'POST':
#         student_form = StudentForms(request.POST, instance=student)
#         if student_form.is_valid():
#             student_form.save()
#             messages.success(request, "Eleve modifié.")
#             return redirect('student:index')
#     else:
#         student_form = StudentForms(instance=student)
        
#     student_form = StudentForms(instance=student)
#     context ["student_form"] = student_form
#     return render(request, "student/form.html", context, )

# @login_required(login_url='auth:login')
# def delete(request, id): 
#     student = Student.objects.get(id=id)
#     student .delete()
#     messages.warning(request, "Eleve supprime.")
#     return redirect('student:index')


# ##################################### Absence ################################







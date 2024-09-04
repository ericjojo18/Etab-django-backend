from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.forms.FormsAbs import AbsenceForm
from student.models.absence import Absence

# Create your views here.

##################################### Absence ################################
@login_required(login_url='auth:login')
def index(request):
    absences = Absence.objects.all()
    
    
    context = {'absences': absences,
               }
    return render(request, "student_absence/index.html", context)


@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        absence_form = AbsenceForm(request.POST)
        print(0)
        if absence_form.is_valid():
            print(2)
            #Student.objects.create(**student_form.cleaned_data)
            print(absence_form.cleaned_data)
            
            absence_form.save()
            messages.success(request, "Eleve ajoute.")
            return redirect('student_absence:index')
        else: 
            print(7)
            absence_form = AbsenceForm()
            print(absence_form.errors)
            messages.error(request, "Eleve non")
            #return render(request, "student/add_student.html" )
    
    absence_form = AbsenceForm()
    context = {'absence_form': absence_form,
               'title': 'Ajouter  un absence'
               }
    return render(request, "student_absence/formAbs.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    absence = Absence.objects.get(id=id)
    context = {'title': 'Modifier un absence'}
    if request.method == 'POST':
        absence_form = AbsenceForm(request.POST, instance=absence)
        if absence_form.is_valid():
            absence_form.save()
            messages.success(request, "Abscence Eleve modifié.")
            return redirect('student_absence:index')
    else:
        absence_form = AbsenceForm(instance=absence)
        
    absence_form = AbsenceForm(instance=absence)
    context ["absence_form"] = absence_form
    return render(request, "student_absence/formAbs.html", context, )

@login_required(login_url='auth:login')
def delete(request, id): 
    absence = Absence.objects.get(id=id)
    absence.delete()
    messages.warning(request, "absence supprime.")
    return redirect('student_absence:index')
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from school.forms.forms_school import SchoolForm
from school.models.school import School

# Create your views here.

##################################### School ################################

def index(request):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(request, "school/index.html", context)

# @login_required(login_url='auth:login')
def add(request):
    if request.method == 'POST':
        school_form = SchoolForm(request.POST)

        if school_form.is_valid():

            #Student.objects.create(**student_form.cleaned_data)
            #print(absence_form.cleaned_data)
            
            school_form.save()
            messages.success(request, "Ecole ajoute.")
            return redirect('school:index')
        else: 
            school_form = SchoolForm()
            #print(appsetting_form.errors)
            messages.error(request, "Ecole non")
            #return render(request, "student/add_student.html" )
        
    
    school_form = SchoolForm()
    context = {'school_form': school_form,
               'title': 'Ajouter  un parametre'
               }
    return render(request, "school/form.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    school = School.objects.get(id=id)
    context = {'title': 'Modifier un absence'}
    if request.method == 'POST':
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            messages.success(request, "Paramétre modifié.")
            return redirect('school:index')
    else:
        school_form = SchoolForm(instance=school)
        check_school = School.objects.all()
        if not check_school:
            return redirect('school:add')
        else:
            return redirect('auth:login')
        
    school_form = SchoolForm(instance=school)
    context ["school_form"] = school_form
    return render(request, "school/form.html", context, )

#la fonction check_settings permet de bloquer l'utilisateur si il n'est pas connecté
def check_settings(request):
    school = School.objects.all()
    if not school:
        return redirect('school:add')
    else:
        return redirect('auth:login')

@login_required(login_url='auth:login')
def delete(request, id): 
    school = School.objects.get(id=id)
    school.delete()
    messages.warning(request, "Parametre supprime.")
    return redirect('school:index')
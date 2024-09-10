from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from school.forms.forms_school import SchoolForm
from school.models.school import School

# Create your views here.

##################################### School ################################

# def index(request):
#     schools = School.objects.all()
#     context = {'schools': schools}
#     return render(request, "school/index.html", context)

#@login_required(login_url='auth:login')
def add(request):
    if request.method == 'POST':
        school_form = SchoolForm(request.POST)

        if school_form.is_valid():

            #Student.objects.create(**student_form.cleaned_data)
            #print(absence_form.cleaned_data)
            
            school_form.save()
            messages.success(request, "Ecole ajoute.")
            return redirect('auth:login')
        else: 
            school_form = SchoolForm()
            #print(appsetting_form.errors)
            messages.error(request, "Ecole non modifié")
            #return render(request, "student/add_student.html" )
    schools = School.objects.all()
    
        
        
    if schools:
        return redirect('auth:login')

    else:
    
        school_form = SchoolForm()
    context = {'school_form': school_form,
               'title': 'Ajouter  une ecole'
               }
    return render(request, "school/form.html", context )

@login_required(login_url='auth:login')
def update(request): 
    
    # school = School.objects.get(id=id)
    #pour recuperer les paramètres d'un seul ecole
    school = School.objects.first()
    context = {'title': 'Modifier une école'}
    if request.method == 'POST':
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            messages.success(request, "Ecole modifié.")
            return redirect('school:index')
    else:
        school_form = SchoolForm(instance=school)
        
        
        
    school_form = SchoolForm(instance=school)
    context ["school_form"] = school_form
    return render(request, "school/form.html", context, )

#la fonction check_settings permet de bloquer l'utilisateur si il n'est pas connecté
def check_schools(request):
    schools = School.objects.all()
    if not schools:
        return redirect('school:add')
    else:
        return redirect('auth:login')

# @login_required(login_url='auth:login')
# def delete(request, id): 
#     school = School.objects.get(id=id)
#     school.delete()
#     messages.warning(request, "Parametre supprime.")
#     return redirect('school:index')
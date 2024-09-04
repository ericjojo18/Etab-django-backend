from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms.role_user_forms import RoleUserForm
from user.models.roleruser import RoleUser

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='auth:login')
def index(request):
    roles = RoleUser.objects.all()
    
    
    context = {'roles': roles,
               }
    return render(request, "role/index.html", context)

@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        role_form = RoleUserForm(request.POST)
        print(0)
        if role_form.is_valid():
            print(2)
            #Student.objects.create(**student_form.cleaned_data)
            print(role_form.cleaned_data)
            
            role_form.save()
            messages.success(request, "Eleve ajoute.")
            return redirect('role:index')
        else: 
            role_form = RoleUserForm()
            print(role_form.errors)
            messages.error(request, "role non")
            #return render(request, "student/add_student.html" )
    
    role_form = RoleUserForm()
    context = {'role_form': role_form,
               'title': 'Ajouter  un role'
               }
    return render(request, "role/form.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    role = RoleUser.objects.get(id=id)
    context = {'title': 'Modifier un role'}
    if request.method == 'POST':
        role_form = RoleUserForm(request.POST, instance=role)
        if role_form.is_valid():
            role_form.save()
            messages.success(request, "role modifié.")
            return redirect('role:index')
    else:
        role_form = RoleUserForm(instance=role)
        
    role_form = RoleUserForm(instance=role)
    context ["role_form"] = role_form
    return render(request, "role/form.html", context, )

@login_required(login_url='auth:login')
def delete(request, id): 
    role = RoleUser.objects.get(id=id)
    role.delete()
    messages.warning(request, "role supprime.")
    return redirect('role:index')
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from school.forms.forms_app_settings import AppSettingForm
from school.models.app_setting import AppSetting
from django.urls import reverse

# Create your views here. 

##################################### AppSetting ################################
# @login_required(login_url='auth:login')
# def index(request):
#     appsetting = AppSetting.objects.all()
#     print(appsetting)
#     context = {'appsetting': appsetting}
#     return render(request, "appsetting/index.html", context)

# @login_required(login_url='auth:login')
def add(request):
    if request.method == 'POST':
        appsetting_form = AppSettingForm(request.POST)

        if appsetting_form.is_valid():

            #Student.objects.create(**student_form.cleaned_data)
            #print(absence_form.cleaned_data)
            
            appsetting_form.save()
            messages.success(request, "Paramétre ajoute.")
            return redirect('school:add')
        else: 
            appsetting_form = AppSettingForm()
            print(appsetting_form.errors)
            messages.error(request, "Paramétre non modifie")
        
    app_settings = AppSetting.objects.all()
        
        # if not app_settings:
        #     return redirect('appsetting:add')
        # else:
        #     return redirect('school:add')
    if app_settings:
            return redirect('auth:login')
    else:
            #return redirect('school:add')
        appsetting_form = AppSettingForm()
    context = {'appsetting_form': appsetting_form,
               'title': 'Ajouter un parametre'
               }
    return render(request, "appsetting/form.html", context )

@login_required(login_url='auth:login')
def update(request, ): 
    
    #appsetting = AppSetting.objects.get(id=id)
    appsetting = AppSetting.objects.first()
    context = {'title': 'Modifier un paramétre'}
    if request.method == 'POST':
        appsetting_form = AppSettingForm(request.POST, instance=appsetting)
        if appsetting_form.is_valid():
            appsetting_form.save()
            messages.success(request, "Paramétre modifié.")
            return redirect('appsetting:index')
    else:
        appsetting_form = AppSettingForm(instance=appsetting)
        
#appsetting_form = AppSettingForm(instance=appsetting)
    context ["appsetting_form"] = appsetting_form
    return render(request, "appsetting/form.html", context, )


def check_settings(request):
    app_settings = AppSetting.objects.all()
    if not app_settings:
        return redirect('appsetting:add')
        
    else:
        return redirect('school:check_school')
        

# @login_required(login_url='auth:login')
# def delete(request, id): 
#     appsetting = AppSetting.objects.get(id=id)
#     appsetting.delete()
#     messages.warning(request, "Parametre supprime.")
#     return redirect(reverse('appsetting:index'))
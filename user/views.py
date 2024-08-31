from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm

# Create your views here.
@login_required(login_url='auth:login')

def index(request, ): 
    users = User.objects.all()
    context = {'users':users}
    
    return render(request,"user/index.html", context)
@login_required(login_url='auth:login')
def add(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user_data_has_error = False
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Cet utilisateur existe déja")
            
        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, "Le mot de passe doit avoir au moins 8 caractères")
            
        if user_data_has_error:
            return redirect('user:add')
        else:
            user = User(username=username)
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()
            
            messages.success(request, "L'utilisateur a bien été ajoute")
        return redirect('user:index')
        #if not username or not password:
            #return render(request, "auth/login.html", {"error": "Veuillez renseigner tous les champs"})
       
        #print(user)
        
    
      
        #print(request.POST) 
        ##if user_form.is_valid():
            
            #print(user_form.cleaned_data)
           # user_form.save()
            #return redirect('user:index')
       # else:
            #user_form = UserForm()
        
        
    #user_from = UserForm()
    context = {
               'title': 'Ajouter  un utilisateur'
               }
    return render(request, "user/form.html", context )
    #return render(request, "user/add_user.html", context)
@login_required(login_url='auth:login')
def update(request, id):
    
    user = User.objects.get(id=id)
    context = {'title': 'Modifier un utilisateur'}
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Utilisateur modifie avec succes.")
            return redirect('user:index', )
    else:
        user_form = UserForm(instance=user)
        
    user_form = UserForm(instance=user)    
    context ["user_form"] = user_form
        
    return render(request, "user/form.html", context )
    #return render(request, "user/update_user.html")
    


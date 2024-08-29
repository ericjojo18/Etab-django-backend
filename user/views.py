from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.

def index(request, ): 
    users = User.objects.all()
    context = {'users':users}
    
    return render(request,"user/index.html", context)

def add(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #if not username or not password:
            #return render(request, "auth/login.html", {"error": "Veuillez renseigner tous les champs"})
        user = User(username=username)
        #print(user)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        return redirect('user:index')
    
      
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

def update(request, id):
    
    user = User.objects.get(id=id)
    context = {'title': 'Modifier un utilisateur'}
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:index', )
    else:
        user_form = UserForm(instance=user)
        
    user_form = UserForm(instance=user)    
    context ["user_form"] = user_form
        
    return render(request, "user/form.html", context )
    #return render(request, "user/update_user.html")
    


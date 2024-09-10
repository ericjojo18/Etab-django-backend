from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from school.models.app_setting import AppSetting
from school.models.school import School

# Create your views here.

#login  required permet de bloquer l'utilisateur si il n'est pas connecté
@login_required(login_url='/')

def index(request):
    return render(request, "dashbord/index.html")

def sing_in(request):
    app_settings = AppSetting.objects.first()
    if not app_settings:
        return redirect('appsetting:check_settings')
    
    school = School.objects.first()
    if not school:
        return redirect('school:check_school')
    
    if request.user.is_authenticated:
        # Si l'utilisateur est déjà connecté, redirigez-le vers le tableau de bord
        return redirect('dashboard:dashboard')
    #
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = authenticate(request, username=username, password=password)
        #print(user)
        
        if user is not None:
            
            login(request, user)
            next = request.GET.get('next','')
            if next:
                return redirect(next)
            else:
                messages.success(request, "Connexion reussie")
                return render(request, "dashbord/index.html")
        
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "auth/login.html")
        
    return render(request, "auth/login.html")

def sing_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return render(request, "auth/login.html", {"error": "Veuillez renseigner tous les champs"})
        user = User(username=username) 
        print(user)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        if user is not None:
            login(request, user)
            return render(request, "dashbord/index.html")
    return render(request, "auth/register.html")

def log_out(request):
    logout(request)
    messages.success(request, "Déconnexion ")
    return redirect('auth:login')
    #return render(request, "auth/logout.html")
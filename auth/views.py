from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, "dashbord/index.html")
def sing_in(request):
   
    
    return render(request, "auth/login.html")

def sing_up(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
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
    return render(request, "auth/logout.html")
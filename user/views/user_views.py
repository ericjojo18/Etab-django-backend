from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from user.models.user import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.forms.user_forms import UserForm

# Create your views here.
@login_required(login_url='auth:login')

def index(request, ): 
    search_field = request.GET.get('search')
    if search_field :
        users = User.objects.filter(username__icontains=search_field)
        context = {
            'users': users,
            'search_field': search_field,
        }
    else:
        users = User.objects.all()
        total_users = users.count()
        context = {
            'users': users,
            'total_users': total_users,
        }
    #users = User.objects.all()
    #context = {'users':users}
    
    return render(request,"user/index.html", context)
@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        user_form =  UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = request.POST.get('password','')
            if password:
                user.set_password(password)
            user.save()
            # role = request.POST.getlist('role')
            # role = user_form.cleaned_data.get('role')
            user.role.add(*user_form.cleaned_data.get('role'))
            
            # if role:
            #     # for r in role:
            #         user.role.add(*role)
            messages.success(request, "L'utilisateur a bien été ajoute")
            return redirect('user:index')
        else:
            user_form = UserForm()
            messages.error()
            
    user_form = UserForm()
    context = {
                'user_form': user_form,
               'title': 'Ajouter  un utilisateur'
               }
    return render(request, "user/form.html", context )
    #return render(request, "user/add_user.html", context)
@login_required(login_url='auth:login')   
def user_status(request, id):
    user = User.objects.get(id=id)

    user.is_active = not user.is_active
    user.save()
    status = "active" if user.is_active else "désactive"
    messages.success(request, f"L'utilisateur a été {status} avec succès.")
    return redirect('user:index', )
    
    #return render(request, "user/form.html", {'user': user} )

@login_required(login_url='auth:login')
def update(request, id):
    
    user = User.objects.get(id=id)
    context = {'title': 'Modifier un utilisateur'}
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = request.POST.get('password','')
            if password:
                user.set_password(password)
            user.save()
            user.role.set(user_form.cleaned_data.get('role'))
            # role = user_form.cleaned_data.get('role')
            
            # if role:
            #     user.role.set(role)
            messages.success(request, "Utilisateur modifie avec succes.")
            return redirect('user:index', )
    else:
        user_form = UserForm(instance=user)
        
    user_form = UserForm(instance=user)    
    context ["user_form"] = user_form
        
    return render(request, "user/form.html", context )
    #return render(request, "user/update_user.html")
    


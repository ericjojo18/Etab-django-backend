from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.forms.formsAdr import AddressForm
from base.models.address import Address
# Create your views here.

@login_required(login_url='auth:login')
def index(request):
    addresse = Address.objects.all()
    context = {'addresse': addresse}
    return render(request, "address/index.html",context)

@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        print(0)
        if address_form.is_valid():
            print(2)
            #Student.objects.create(**student_form.cleaned_data)
            print(address_form.cleaned_data)
            
            address_form.save()
            messages.success(request, "Adresse ajoute.")
            return redirect('base:index')
        else: 
            print(7)
            address_form = AddressForm()
            print(address_form.errors)
            messages.error(request, "Eleve non")
            #return render(request, "student/add_student.html" )
    
    address_form = AddressForm()
    context = {'address_form': address_form,
               'title': 'Ajouter  un adresse'
               }
    return render(request, "address/form.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    address = Address.objects.get(id=id)
    context = {'title': 'Modifier un adresse'}
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=address)
        if address_form.is_valid():
            address_form.save()
            messages.success(request, "Adresse modifié.")
            return redirect('base:index')
    else:
        address_form = AddressForm(instance=address)
        
    address_form = AddressForm(instance=address)
    context ["address_form"] = address_form
    return render(request, "address/form.html", context, )

@login_required(login_url='auth:login')
def delete(request, id):
        address= Address.objects.get(id=id)
        address.delete()
        messages.warning(request, "Adresse supprime.")
        return redirect('base:index')
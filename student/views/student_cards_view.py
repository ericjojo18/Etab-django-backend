from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models.studentcards import StudentCards
from student.forms.formsStudC import StudentCardForm

########################### STUDENTS CARDS ##########################

@login_required(login_url='auth:login')
def index(request):
    student_cards = StudentCards.objects.all()
    context = {'student_cards': student_cards,
               }
    return render(request, "student_cards/index.html", context)

@login_required(login_url='auth:login')
def add(request):
    
    if request.method == 'POST':
        stucards_form = StudentCardForm(request.POST)

        if stucards_form.is_valid():
            #Student.objects.create(**student_form.cleaned_data)
            print(stucards_form.cleaned_data)
            
            stucards_form.save()
            messages.success(request, "Carte ajoute.")
            return redirect('studentcard:index')
        else: 
            stucards_form = StudentCardForm()
            messages.error(request, "Eleve non")
            #return render(request, "student/add_student.html" )
    
    stucards_form = StudentCardForm()
    context = {'stucards_form': stucards_form,
               'title': 'Ajouter une carte etudiant'
               }
    return render(request, "student_cards/formCard.html", context )

@login_required(login_url='auth:login')
def update(request, id): 
    
    studentcard = StudentCards.objects.get(id=id)
    context = {'title': 'Modifier un absence'}
    if request.method == 'POST':
        stucards_form = StudentCardForm(request.POST, instance=studentcard)
        if stucards_form.is_valid():
            stucards_form.save()
            messages.success(request, "Carte modifié.")
            return redirect('studentcard:index')
    else:
        stucards_form = StudentCardForm(instance=studentcard)
        
    stucards_form = StudentCardForm(instance=studentcard)
    context ["stucards_form"] = stucards_form
    return render(request, "student_cards/formCard.html", context, )

@login_required(login_url='auth:login')
def delete(request, id): 
    studentcard = StudentCards.objects.get(id=id)
    studentcard.delete()
    messages.warning(request, "Carte supprime.")
    return redirect('studentcard:index')

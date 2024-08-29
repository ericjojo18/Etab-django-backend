from django import forms
from .models import Teacher
class TeacherForm(forms.Form):
    
    VACANT = {
        "True": "Oui",
        "False": "Non",
    }
    
    first_name = forms.CharField(max_length=100,label="Nom", 
                                 widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nom","required": True}))
    last_name = forms.CharField(max_length=100, label="Prénom",
                                widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre prénom", "label":"Prenom","required": True}))
    city = forms.CharField(max_length=100, label="Ville",
                           widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre ville","required": True}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control","type":"date"}))
    phone = forms.CharField(max_length=10,label="Numéro de téléphone",
                           widget=forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre telephone", "required": True}))
    birth_date = forms.DateField(label= "Date de naissance", widget=forms.DateInput(attrs={"class": "form-control","type":"date"}) )
    is_vacant = forms.ChoiceField(choices=VACANT, label="Vacant", widget=forms.RadioSelect(attrs={}))
    matter = forms.CharField(max_length=30,label="Matières enseignéee", widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre matière","required": True}))
    next_class = forms.CharField(max_length=30, label="Prochaine classe",widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre prochaine cours","required": True}) )
    subject_next_meeting = forms.CharField(max_length=100, label="Sujet prochain cours",widget=forms.TextInput(attrs={"class": "form-control", 
                                                                                                                      "placeholder":"Entrer votre prochaine cours","required": True}) )

class TeacherForms(forms.ModelForm):
        class Meta:
            model = Teacher
            fields = ['first_name', 'last_name', 'city', 'birth_date', 'phone',
                      'is_vacant', 'matter', 'next_class', 'subject_next_meeting']
            
            labels = {'first_name':'Nom', 'last_name':'Prenom', 'city':'Ville',
                      'birth_date':'Date de naissance', 'phone':'Numéro de numéro', 
                      'is_vacant':'Vacant', 'matter':'Matières enseignée',
                      'next_class':'Prochaine classe', 'subject_next_meeting':'Sujet prochain cours'}
           
            widgets= {
                'first_name':  forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre nom","required": True}),
                'last_name': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre prénom", "label":"Prenom","required": True}),
                'city': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre ville","required": True}),
                'birth_date': forms.DateInput(attrs={"class": "form-control","type":"date"}),
                'phone' : forms.NumberInput(attrs={"class": "form-control",
                                                               "placeholder":"Entrer votre telephone", "required": True}),
                'is_vacant': forms.RadioSelect(choices=TeacherForm.VACANT,attrs={}),
                'matter': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre matière","required": True}),
                'next_class': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre prochaine cours","required": True}),
                'subject_next_meeting': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre prochaine cours","required": True})          
            }
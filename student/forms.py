from django import forms
from .models import Student


class StudentForm(forms.Form):
    
    CLASSROM = {
        "6e": "Sixième",
        "5e": "Cinquième",
        "4e": "Quatrième",
        "3e": "Troisième",
        "2nd A": "Seconde A",
        "2nd C": "Seconde C",
        "1er A": "Premier A",
        "1er C": "Premier C",
        "1er D": "Premier D",
        "Tle A": "Terminaale A",
        "Tle C": "Terminaale C",
        "Tle D": "Terminaale D",
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
    birth_date = forms.DateField(label= "Date de naissance",    widget=forms.DateInput(attrs={"class": "form-control","type":"date"}) )
    classrom = forms.CharField(max_length=10,label="Classe" ,widget= forms.Select(attrs={"class": "form-control", "label":"Classe",},choices=CLASSROM))
    registration_number = forms.CharField(max_length=30, label="Matricule",
                           widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre matricule","required": True}))
    
class StudentForms(forms.ModelForm):
    
        class Meta:
            model = Student
            fields = ['first_name', 'last_name', 'city', 'birth_date', 'phone', 'classrom', 'registration_number']
            labels = {'first_name':'Nom', 'last_name':'Prenom', 'city':'Ville', 
                      'birth_date':'Date de naissance', 'phone':'Numéro de numéro', 'classrom':'Classe', 'registration_number':'Matricule'}
            widgets= {
                 'first_name':  forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre nom","required": True}),
                'last_name': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre prénom", "label":"Prenom","required": True}),
                'city': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre ville","required": True}),
                'birth_date': forms.DateInput(attrs={"class": "form-control","type":"date"}),
                'phone' : forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre telephone", "required": True}),
                'classrom': forms.Select(attrs={"class": "form-control", "label":"Classe",},choices=StudentForm.CLASSROM),
                'registration_number': forms.TextInput(attrs={"class": "form-control", 
                                                            "placeholder":"Entrer votre matricule","required": True})          
            }
    

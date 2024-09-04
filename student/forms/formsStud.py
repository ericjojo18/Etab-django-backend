from django import forms
from student.models.student import Student
from base.models.helpers.enum import Gender
from base.models.address import Address

class StudentForm(forms.Form):
    
           
    first_name = forms.CharField(max_length=100,label="Nom", 
                                 widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nom","required": True}))
    last_name = forms.CharField(max_length=100, label="Prénom",
                                widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre prénom", "label":"Prenom","required": True}))
    city = forms.CharField(max_length=100, label="Ville",
                           widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre ville","required": True}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control","type":"date"}))
    phone_number = forms.CharField(max_length=10,label="Numéro de téléphone",
                           widget=forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre telephone", "required": True}))
    birth_date = forms.DateField(label= "Date de naissance",    widget=forms.DateInput(attrs={"class": "form-control","type":"date"}) )
    registration_number = forms.CharField(max_length=30, label="Matricule",
                           widget=forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre matricule","required": True}))
    
class StudentForms(forms.ModelForm):
    
        class Meta:
            model = Student
            exclude = ['user', 'created_at', 'updated_at','address','status']
            fields = ['first_name', 'last_name','birthday', 'phone_number','url_picture','gender' , 'matricule', 'phone_number_father' ]
            labels = {'first_name':'Nom', 'last_name':'Prenom', 'birthday':'Date de naissance', 'phone_number':'Numéro de numéro', 'url_picture':'image', 
                         'matricule':'Matricule', 'phone_number_father': 'Numero du pére'}
            widgets= {
                'first_name':  forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre nom","required": True}),
                'last_name': forms.TextInput(attrs={"class": "form-control",
                                                    "placeholder":"Entrer votre prénom", "label":"Prenom","required": True}),
                'birthday': forms.DateInput(attrs={"class": "form-control","type":"date"}),
                'phone_number' : forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre telephone", "required": True}),
                'url_picture': forms.URLInput(attrs={"class": "form-control", "placeholder":"Entrer votre ville","required": True}),
                
                #'gender': forms.Select(attrs={"class": "form-control", },choices=Gender),
                
                #'address': forms.Select(attrs={"class": "form-control",},choices=Address),
                'matricule': forms.TextInput(attrs={"class": "form-control", 
                                                            "placeholder":"Entrer votre matricule","required": True}),   
                'phone_number_father': forms.NumberInput(attrs={"class": "form-control", 
                                                            "placeholder":"Entrer votre matricule","required": True}) ,
                'gender': forms.RadioSelect(attrs={"class": "custom-radio", }),                
            }
    

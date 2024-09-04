from django import forms
from .models.teacher import Teacher


class TeacherForms(forms.ModelForm):
        class Meta:
            model = Teacher
            fields = ['first_name', 'last_name', 'birthday', 'phone_number', 'available',
                      'url_picture', 'gender', 'address', 'speciality']
            exclude = ['user', 'address', 'created_at', 'updated_at', 'status']
            
            labels = {'first_name':'Nom', 'last_name':'Prenom', 'phone_number':'Numéro de numéro',
                      'birth_date':'Date de naissance',  'speciality':'Sujet prochain cours'}
           
            widgets= {
                'first_name':  forms.TextInput(attrs={"class": "form-control","placeholder":"Entrer votre nom","required": True}),
                'last_name': forms.TextInput(attrs={"class": "form-control","placeholder":"Entrer votre prénom", "label":"Prenom","required": True}),
                'url_picture': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre ville","required": True}),
                'birthday': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
                'phone_number' : forms.NumberInput(attrs={"class": "form-control",
                                                               "placeholder":"Entrer votre telephone", "required": True}),
                #'available': forms.RadioSelect(choices=TeacherForm.VACANT,attrs={}),
                'speciality': forms.TextInput(attrs={"class": "form-control","placeholder":"Entrer votre matière","required": True}),
                'gender': forms.RadioSelect(attrs={"class": "custom-radio", }),          
            }
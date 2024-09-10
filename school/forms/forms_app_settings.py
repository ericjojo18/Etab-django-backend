from typing import Any
from django import forms
from school.models.app_setting import AppSetting
from django.contrib.auth.hashers import make_password

class AppSettingForm(forms.ModelForm):
    
    
    class Meta:
        model = AppSetting
        fields = "__all__"
        labels = {'smtp_username': 'smpt_nom_utilisateur', 'smtp_password':'smtp mot de passe'}
        widgets ={
            'smtp_server': forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre serveur", "required": True}),
            'smtp_port': forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre port", "required": True}),
            'smtp_username': forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nom du serveur", "required": True}),
            'smtp_password': forms.PasswordInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer le mot de passe du serveur", "required": True}),
            
        }
        
    def save(self, commit=True): 
        appsetting_smtp_password = super().save(commit=False)
        appsetting_smtp_password.smtp_password = make_password(appsetting_smtp_password.smtp_password)
        if commit:
            appsetting_smtp_password.save()
        return appsetting_smtp_password
    
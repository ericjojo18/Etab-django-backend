from django import forms
from school.models.app_setting import AppSetting

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
            'smtp_password': forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer le mot de passe du serveur", "required": True}),
            
        }
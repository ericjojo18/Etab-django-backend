from django import forms
from school.models.school import School
from school.models.app_setting import AppSetting

class SchoolForm(forms.ModelForm):
    
    class Meta:
        model = School
        fields = "__all__"
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nom d'école", "required": True}),
            'url_logo': forms.URLInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre url de l'image", "required": True}),
            'app_id': forms.Select(attrs={"class": "form-control",  "required": True}, choices=AppSetting)
        }
        
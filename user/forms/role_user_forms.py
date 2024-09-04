from django import forms
from user.models.roleruser import RoleUser

class RoleUserForm(forms.ModelForm):
    class Meta:
        model = RoleUser
        fields = ["role"]
        
        widgets = {
            'role': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre role", "required": True})
        }
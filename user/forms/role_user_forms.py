from django import forms
from user.models.role_model import RoleModel

class RoleUserForm(forms.ModelForm):
    class Meta:
        model = RoleModel
        fields = ["name"]
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre role", "required": True})
        }
from django import forms
#from .models import User
from django.contrib.auth.models import User

class UserForms(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    creation_date = forms.DateTimeField()


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
    class Meta:
        model = User
        fields = ['username', 'password',]
        labels = {'username': 'Nom d\'utilisateur', 'password': 'Mot de passe'}
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre nom d\'utilisateur', 'required': True}),
            
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre mot de passe', 'required': True}),
        }
         
       # exclude = ['creat_at']
        
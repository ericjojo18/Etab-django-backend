from  django import forms
from user.models.user import User
from user.models.roleruser import RoleUser
#from school.models.school import School

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance is not None:
            self.fields['username'].widget.attrs.update({
                'readonly': 'readonly',
                'label': 'azy'
                
            })

            self.fields['password'].required = False
            
        self.fields['username'].help_text = ''
    
    class Meta:
        model = User
        fields = ["username","password","role","school",]
        
        widgets = {
            'role': forms.CheckboxSelectMultiple,
            #'school': forms.Select(attrs={"class": "form-control", "placeholder":"Entrer votre role", "required": True},choices=School),
            'username': forms.TextInput(attrs={"class": "form-control", "placeholder":"Entrer votre pseudo", "required": True}),
            'password': forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Entrer votre mot de passe", "required": True})
                
        }
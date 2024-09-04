from django import forms
from base.models.address import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        
        fields = {'city','street', 'country'}
        exclude = ['created_at', 'updated_at', 'status']
        widgets = {
            'city': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre ville","required": True}),
            'street': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre ville","required": True}),
            'country': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre pays","required": True}),
        }
        
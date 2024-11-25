from django import forms
from base.models.address_model import AddressModel

class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        
        fields = {'city','street', 'country'}
        exclude = ['created_at', 'updated_at', 'status']
        # label = {'city': 'Ville', 'street': 'Rue', 'country': 'Pays'}
        widgets = {
            'city': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre ville","required": True}),
            'street': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre ville","required": True}),
            'country': forms.TextInput(attrs={"class": "form-control",
                                                      "placeholder":"Entrer votre pays","required": True}),
        }
        
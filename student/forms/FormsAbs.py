from django import forms
from student.models.absence import Absence
from student.models.student import Student

class AbsenceForm(forms.ModelForm):
    
    class Meta:
        model = Absence
        fields = ("student","absence_date","absence_number")
        labels = {'student':'Eleve'}
        widgets = {
            'student': forms.Select(attrs={"class": "form-control",},choices=Student),
            'absence_date': forms.DateInput(attrs={"class": "form-control","type":"date"}),
            'adsence_number': forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nombre", "required": True}),
            
        }

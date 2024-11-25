from django import forms
from student.models.absence_model import AbsenceModel
from student.models.student_model import StudentModel

class AbsenceForm(forms.ModelForm):
    
    class Meta:
        model = AbsenceModel
        fields = ("student","absence_date","absence_number")
        labels = {'student':'Eleve'}
        widgets = {
            'student': forms.Select(attrs={"class": "form-control",},choices=StudentModel),
            'absence_date': forms.DateInput(attrs={"class": "form-control","type":"date"}),
            'adsence_number': forms.NumberInput(attrs={"class": "form-control", 
                                                               "placeholder":"Entrer votre nombre", "required": True}),
            
        }

from django import forms
from student.models.studentcards import StudentCards
from datetime import datetime

class StudentCardForm(forms.ModelForm):
    
    class Meta:
        model = StudentCards
        fields = ['student','reference','issue_date','expiration_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date','max': datetime.now().strftime('%Y-%m-%d')}),
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'min': datetime.now().strftime('%Y-%m-%d')}),
        }
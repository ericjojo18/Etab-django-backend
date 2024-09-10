from django import forms
from student.models.student import Student
from teacher.models.teacher import Teacher
from user.models.user import User


class ReportForm(forms.Form):
    
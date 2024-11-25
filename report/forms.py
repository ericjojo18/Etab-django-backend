from django import forms
from student.models.student_model import Student
from teacher.models.teacher_model import Teacher
from user.models.user_model import User


class ReportForm(forms.Form):
    
from django.contrib import admin
from student.models.student import Student
from student.models.absence import Absence
from student.models.studentcards import StudentCards


# Register your models here.
admin.site.register(Student)
admin.site.register(Absence)
admin.site.register(StudentCards)


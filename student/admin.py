from django.contrib import admin
from student.models.student_model import StudentModel
from student.models.absence_model import AbsenceModel
from student.models.student_cards_model import StudentCardsModel


# Register your models here.
admin.site.register(StudentModel)
admin.site.register(AbsenceModel)
admin.site.register(StudentCardsModel)


from django.db import models
from student.models.student_model import StudentModel

class AbsenceModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE,null=True,blank=True, related_name="student_absence_ids")
    absence_date = models.DateField()
    absence_number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Absence {self.absence_number} on {self.absence_date} for Student ID {self.student}"
    
    
    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
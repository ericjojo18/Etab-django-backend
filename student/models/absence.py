from django.db import models

class Absence(models.Model):
    studend_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name="student_absence_ids")
    absence_date = models.DateField()
    absence_number = models.IntegerField()
    
    def __str__(self):
        return self.studend_id, self.absence_date, self.absence_number
    
    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
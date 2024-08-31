from django.db import models

class StudentCards(models.Model):
    studend_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name="student_studentcard_ids")
    reference = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
     
    def __str__(self) :
        return self.studend_id, self.reference, self.issue_date, self.issue_date, self.expiration_date
    
    class Meta:
        verbose_name = "StudentCard"
        verbose_name_pluriel = "StudentCarts"
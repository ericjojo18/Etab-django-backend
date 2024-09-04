from django.db import models
from student.models.student import Student

class StudentCards(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)
    reference = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
     
    def __str__(self) :
        return f"{self.student}, {self.reference}, {self.issue_date}, {self.issue_date}, {self.expiration_date}"
    
    class Meta:
        verbose_name = "StudentCard"
        verbose_name_plural = "StudentCarts"
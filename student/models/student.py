from django.db import models
from base.models.helpers.person import Person

class Student(Person):
    matricule = models.CharField(max_length=255)
    phone_number_father = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
from django.db import models
from base.models.person import Person

class Student(Person):
    matricule = models.CharField(max_length=30)
    phone_number_father = models.CharField(max_length=10)
    
    def __str__(self):
        return self.matricule, self.phone_number_father
    
    class Meta:
        verbose_name = "Student"
        verbose_name = "Students"
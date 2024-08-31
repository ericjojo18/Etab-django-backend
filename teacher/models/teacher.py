from django.db import models
from base.models.person import Person

# Notre modéle teacher qui herite des attributs de la classe abstraits person
class Teacher(Person):
    available = models.BooleanField()
    speciality = models.CharField()
    
    def __str__(self):
        return self.available, self.speciality
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plurial = "Teachers"

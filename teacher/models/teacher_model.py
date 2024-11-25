from django.db import models
from base.models.person_model import PersonModel

# Notre modéle teacher qui herite des attributs de la classe abstraits person
class TeacherModel(PersonModel):
    available = models.BooleanField()
    speciality = models.CharField(max_length=100)
    
    def __str__(self):
        return self.available, self.speciality
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

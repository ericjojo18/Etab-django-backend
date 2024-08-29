from django.db import models
from datetime import date
from django.utils.text import slugify
# Create your models here.

class Teacher(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)
    is_vacant = models.BooleanField()
    matter = models.CharField(max_length=30)
    next_class = models.CharField(max_length=30)
    subject_next_meeting = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    
    
    def __str__(self):
        return self.first_name, self.last_name, self.city, self.birth_date, self.phone, self.is_vacant, self.matter, self.next_class, self.subject_next_meeting
    
    def age(self):
        
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    class Meta: 
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
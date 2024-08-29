from django.db import models
from datetime import date  
from django.utils.text import slugify 
# Create your models here.
class Student(models.Model):
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=10)
    classrom = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        #pour eviter les doublons dans le slug
        if not self.slug:
            self.slug = slugify(self.first_name)
            original_slug = slugify(self.first_name)
            for i in range(1, 100):
                if not Student.objects.filter(slug=original_slug).exists():
                    break
                original_slug = f"{original_slug}-{i}"
            super(Student, self).save(*args, **kwargs)
        self.slug = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.first_name, self.last_name, self.city, self.birth_date, self.phone, self.classrom, self.registration_number
    
    def age(self):
        
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    class Meta: 
        verbose_name = "Student"
        verbose_name_plural = "Students"
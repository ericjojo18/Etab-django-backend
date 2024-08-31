from django.db import models

# Create your models here.

class Person(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    url_picture = models.CharField()
    gender = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.first_name, self.last_name, self.birthday, self.phone_number, self.phone_number, self.url_picture, self.gender
    
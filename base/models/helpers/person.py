from django.db import models
from base.models.helpers.enum import Gender
from base.models.helpers.date_time_model import DateTimeModel
from base.models.address import Address
from user.models.user import User
# Create your models here.

class Person(DateTimeModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    url_picture = models.URLField(max_length=200)
    gender = models.CharField(max_length=6, choices=Gender.choices)
    
    
    class Meta:
        abstract = True
        
    #def __str__(self):
        #return self.first_name, self.last_name, self.birthday, self.phone_number, self.phone_number, self.url_picture, self.gender
    
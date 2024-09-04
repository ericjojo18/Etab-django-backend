from django.db import models

from user.models.roleruser import RoleUser
from school.models.school import School
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel

class User(AbstractUser):
    role = models.ForeignKey(RoleUser, on_delete=models.SET_NULL, null=True,blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True,blank=True)
    #pseudo = models.CharField(max_length=100)
    #password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.username}, "
    
    class Meta:
        verbose_name = "User" 
        verbose_name_plural = "Users"
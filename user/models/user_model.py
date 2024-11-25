from django.db import models

from user.models.role_model import RoleModel
from school.models.school_model import SchoolModel
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel

class UserModel(AbstractUser):
    role = models.ManyToManyField(RoleModel, related_name='users')
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE,null=True,blank=True)
    #pseudo = models.CharField(max_length=100)
    #password = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in self.__dict__:
            if self.password and not self.password.startswith('pbkdf2_'):
                self.set_password(self.password)
        super(UserModel, self).save(*args, **kwargs)
    
    def __str__(self): 
        return f"{self.username}"

    def get_role_name(self):
        return self.role.name if self.role else None
    
    class Meta:
        verbose_name = "User" 
        verbose_name_plural = "Users"
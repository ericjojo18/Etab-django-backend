from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

class RoleUser(DateTimeModel):
    role = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.role
    
    class Meta:
        verbose_name = "RoleUser"
        verbose_name_plural = "RoleUsers"
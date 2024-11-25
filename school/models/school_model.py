from django.db import models
from school.models.app_setting_model import AppSettingModel
class SchoolModel(models.Model):
    app = models.OneToOneField(AppSettingModel, on_delete=models.CASCADE,null=True,blank=True, related_name="school_app_id")
    name = models.CharField(max_length=100)
    url_logo = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.name}, {self.url_logo}"
    
    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
    

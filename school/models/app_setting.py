from django.db import models

class AppSetting(models.Model):
    smtp_server = models.CharField(max_length=200)
    smtp_port = models.CharField(max_length=200)
    smtp_username = models.CharField(max_length=200)
    smtp_password = models.CharField(max_length=100)
    
    def __str__(self):
        return f" {self.smtp_username}"
    
    class Meta:
        verbose_name = "AppSetting"
        verbose_name_plural = "AppSettings"
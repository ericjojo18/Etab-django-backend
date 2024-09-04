from django.contrib import admin
from user.models.user import User
from user.models.roleruser import RoleUser
from school.models.school import School
from school.models.app_setting import AppSetting

# Register your models here.

admin.site.register(User) 
admin.site.register(RoleUser) 
admin.site.register(School) 
admin.site.register(AppSetting) 
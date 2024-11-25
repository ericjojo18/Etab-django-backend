from django.contrib import admin
from user.models.user_model import UserModel
from user.models.role_model import RoleModel
from school.models.school_model import SchoolModel
from school.models.app_setting_model import AppSettingModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(RoleModel)
admin.site.register(SchoolModel)
admin.site.register(AppSettingModel)
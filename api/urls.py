from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewset.student_api_views import student_api
from .viewset.teacher_api_views import teacher_api


router = routers.DefaultRouter()
router.register(r'students', student_api, basename="student")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('students', student_api),
    path('teachers', teacher_api)
]
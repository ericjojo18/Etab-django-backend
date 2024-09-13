from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewset.student_api_views import student_api, student_api_view_detail
from .viewset.teacher_api_views import teacher_api, teacher_api_view_detail
from .viewset.user_api_views import user_api, user_api_view_detail


router = routers.DefaultRouter()
router.register(r'students', student_api, basename="student")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('students', student_api),
    path('teachers', teacher_api),
    path('users', user_api),
    
    # path('student', student_api_view_detail),
    path('student/<int:pk>', student_api_view_detail),
    path('teacher/<int:pk>', teacher_api_view_detail),
    path('user/<int:pk>', user_api_view_detail),
]
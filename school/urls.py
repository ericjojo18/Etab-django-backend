from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", include('school.Urls.app_setting_urls'), ),
    path("school/", include('school.Urls.school_urls'), ),
] 

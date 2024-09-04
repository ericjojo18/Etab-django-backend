from django.urls import path
from school.views.school_views import index,check_settings, add, update, delete
from django.conf import settings
from django.conf.urls.static import static

app_name = "school"

urlpatterns = [
    
    path("",check_settings, name="check_school"),
    path('index/',index, name="index"),
    path("ajout_school", add, name="add"),
    path("modif_school/<int:id>", update, name="update"),
    path("supprimer_school/<int:id>", delete, name="delete"),
]  

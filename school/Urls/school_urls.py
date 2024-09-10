from django.urls import path
from school.views.school_views import check_schools, add, update 
from django.conf import settings
from django.conf.urls.static import static

app_name = "school"

urlpatterns = [
    
    path("",check_schools, name="check_school"),
    # path('index/',index, name="index"),
    path("ajout_school", add, name="add"),
    path("modif_school/", update, name="update"),
    # path("supprimer_school/<int:id>", delete, name="delete"),
]  

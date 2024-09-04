from django.urls import path
from school.views.app_settings_views import  index,check_settings, add, update
from django.conf import settings
from django.conf.urls.static import static

app_name = "appsetting"
urlpatterns = [
    path("", check_settings, name="check_settings"),
    path("list", index, name="index"),
    path("ajout_app", add, name="add"),
    path("modif_app_setting/<int:id>/", update, name="update"),
    # path("supprimer_app/<int:id>/", delete, name="delete"),
]   

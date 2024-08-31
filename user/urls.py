from django.urls import path
from user.views import index, add, update
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"
urlpatterns = [
    path('',index, name="index"),
    path('ajouter_utilisateur',add, name="add"),
    path('modifier_utilisateur/<int:id>/',update, name="update"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


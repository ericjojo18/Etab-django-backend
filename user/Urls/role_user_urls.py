from django.urls import path
from user.views.role_user_views import index, add, update, delete
from django.conf import settings
from django.conf.urls.static import static

app_name = "role"
urlpatterns = [
    path('',index, name="index"),
    path("ajout_role", add, name="add"),
    path("modif_role/<int:id>/", update, name="update"),
    path("supprimer_role/<int:id>/", delete, name="delete"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
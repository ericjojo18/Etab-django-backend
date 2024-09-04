from django.urls import path
from  base.views import index, add, update, delete
from django.conf import settings
from django.conf.urls.static import static

app_name = "base"

urlpatterns = [
    path("", index, name="index"),
    path("ajout_address", add, name="add"),
    path("modif_adresse/<int:id>", update, name="update"),
    path("supprimer_adresse/<int:id>", delete, name="delete")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

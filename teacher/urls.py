from django.urls import path
from teacher.views import index, add, update, delete
from django.conf import settings
from django.conf.urls.static import static

app_name = "teacher"
urlpatterns = [ 
    path('',index, name="index"),
    path('ajouter_professeur/', add, name="add"),
    path('modifier_professeur/<int:id>/', update, name="update"),
    path('supprimer_professeur/<int:id>/', delete, name="delete"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


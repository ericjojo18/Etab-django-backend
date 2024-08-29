from django.urls import path
from teacher.views import index, add, update, delete

app_name = "teacher"
urlpatterns = [ 
    path('',index, name="index"),
    path('ajouter_professeur/', add, name="add"),
    path('modifier_professeur/<int:id>/', update, name="update"),
    path('supprimer_professeur/<int:id>/', delete, name="delete"),
]

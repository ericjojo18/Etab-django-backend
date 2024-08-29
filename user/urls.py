from django.urls import path
from user.views import index, add, update

app_name = "user"
urlpatterns = [
    path('',index, name="index"),
    path('ajouter_utilisateur',add, name="add"),
    path('modifier_utilisateur/<int:id>/',update, name="update"),
    
]


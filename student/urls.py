from django.urls import path
from student.views import index, add, update, delete

#nom de notre application dans l'url (localhost:8000/eleve/) par la variable app_name
app_name = "student"

urlpatterns = [
    path("", index, name="index"),
    
    path("ajout_eleve", add, name="add"),
    path("modif_eleve/<int:id>", update, name="update"),
    path("supprimer_eleve/<int:id>", delete, name="delete")
]
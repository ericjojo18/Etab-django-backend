from django.urls import path

from student.views.student_cards_view import index, add, update, delete


#nom de notre application dans l'url (localhost:8000/eleve/) par la variable app_name
app_name = "studentcard"

urlpatterns = [
    ################ Absence #########################
    path("", index, name="index"),
    path("ajout_cards/", add, name="add"),
    path("modif_cards/<int:id>", update, name="update"),
    path("supprimer_cards/<int:id>", delete, name="delete")
]
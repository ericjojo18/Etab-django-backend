from django.urls import path
from student.views.absence_views import index, add, update, delete


#nom de notre application dans l'url (localhost:8000/eleve/) par la variable app_name
app_name = "student_absence"

urlpatterns = [
    ################ Absence #########################
    path('', index, name="index"),
    path('ajout_Abs/', add, name="add"),
    path("modif_Abs/<int:id>", update, name="update"),
    path("supprimer_Abs/<int:id>", delete, name="delete")
]
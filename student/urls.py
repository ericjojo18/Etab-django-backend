from django.urls import path, include


#nom de notre application dans l'url (localhost:8000/eleve/) par la variable app_name


urlpatterns = [
    path('', include('student.Urls.students_urls')),
    path('absence/', include('student.Urls.absence_urls')),
    path('carte/', include('student.Urls.student_card_urls'))
    # path('absence/', include('student.Urls.absence_urls')),
    # path("StudentCards/", include('student.Urls.student_card_urls')),
    
] 
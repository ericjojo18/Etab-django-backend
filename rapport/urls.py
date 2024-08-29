from django.urls import path
from rapport.views import index

app_name ="rapport"

urlpatterns = [
    path('', index, name="rapport"),
    
]

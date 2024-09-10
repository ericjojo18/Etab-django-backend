from django.urls import path
from user.views.user_views import index, add, update, user_status
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"
urlpatterns = [
    path('',index, name="index"),
    path('ajouter_utilisateur',add, name="add"),
    path('modifier_utilisateur/<int:id>/',update, name="update"),
    path('status-user/<int:id>/', user_status, name="user_status"),
    
] 
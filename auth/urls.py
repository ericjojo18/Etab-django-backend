from django.urls import path
from django.contrib.auth import views
from auth.views  import  sing_in, sing_up, log_out

app_name = "auth"

urlpatterns = [
    path('', sing_in, name="login"),
    path('register', sing_up, name="register"),
    path('log_out', log_out, name="logout"),
]
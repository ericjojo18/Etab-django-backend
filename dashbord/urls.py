from django.urls import path
from dashbord.views import index

app_name = "dashboard"
urlpatterns = [
    path("", index, name="dashboard")
]
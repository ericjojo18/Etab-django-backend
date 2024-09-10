from django.urls import path
from rapport.views import index, generate_report

app_name ="rapport"

urlpatterns = [
    path('', index, name="rapport"),
    path('generate-report',generate_report, name='generate')
]

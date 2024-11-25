from django.urls import path
from report.views import index, generate_report

app_name ="report"

urlpatterns = [
    path('', index, name="report"),
    path('generate-report',generate_report, name='generate')
]

from rest_framework import viewsets, permissions
from student.models.absence_model import AbsenceModel
from api.serializers.student_absence_serializer import StudentAbsenceSerializer


class StudentAbsenceViewSet(viewsets.ModelViewSet):
    queryset = AbsenceModel.objects.all()
    serializer_class = StudentAbsenceSerializer
    permission_classes = [permissions.AllowAny]
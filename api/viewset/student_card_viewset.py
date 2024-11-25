from rest_framework import viewsets, permissions

from student.models.student_cards_model import StudentCardsModel
from api.serializers.student_cards_serializer import StudentCardsSerializer


class StudentCardViewSet(viewsets.ModelViewSet):
    queryset = StudentCardsModel.objects.all()
    serializer_class = StudentCardsSerializer
    permission_classes = [permissions.AllowAny]
    
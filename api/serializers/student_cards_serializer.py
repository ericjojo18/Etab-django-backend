from rest_framework import serializers
from student.models.student_cards_model import StudentCardsModel


class StudentCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCardsModel
        fields = "__all__"
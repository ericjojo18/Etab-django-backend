from rest_framework import serializers
from student.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
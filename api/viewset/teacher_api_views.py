from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from teacher.models.teacher import Teacher
from api.serializers.teacher_serializers import TeacherSerializer


@csrf_exempt
def teacher_api(request):
    
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer_class = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
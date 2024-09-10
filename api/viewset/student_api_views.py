from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from student.models.student import Student
from api.serializers.student_serializers import StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     students = Student.objects.filter(statue=True)
#     serializer_class = StudentSerializer(students, many=True)
#     return JsonResponse(serializer_class.data)

@csrf_exempt
def student_api(request):
    
    if request.method == 'GET':
        students = Student.objects.all()
        serializer_class = StudentSerializer(students, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)        # Check if the serializer is valid
            # Save the serializer
            # Return the serialized data

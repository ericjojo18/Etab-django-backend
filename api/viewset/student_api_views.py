from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
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


@csrf_exempt
def student_api_view_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        students = Student.objects.all()
        serializer_class = StudentSerializer(students, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
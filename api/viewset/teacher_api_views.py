from rest_framework import viewsets, permissions
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from teacher.models.teacher_model import TeacherModel
from api.serializers.teacher_serializer import TeacherSerializer



class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = TeacherModel.objects.all()
    permission_classes = [permissions.AllowAny]

# @csrf_exempt
# def teacher_api(request):
    
#     if request.method == 'GET':
#         teachers = Teacher.objects.all()
#         serializer_class = TeacherSerializer(teachers, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TeacherSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    

# @csrf_exempt
# def teacher_api_view_detail(request, pk):
#     try:
#         teacher = Teacher.objects.get(pk=pk)
#     except Teacher.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         teachers = Teacher.objects.all()
#         serializer_class = TeacherSerializer(teachers, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TeacherSerializer(teacher, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         teacher.delete()
#         return HttpResponse(status=204)
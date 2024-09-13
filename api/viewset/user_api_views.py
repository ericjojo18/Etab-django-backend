from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from user.models.user import User
from api.serializers.user_serializers import UserSerializer


@csrf_exempt
def user_api(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer_class = UserSerializer(users, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def user_api_view_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        users = User.objects.all()
        serializer_class = UserSerializer(users, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
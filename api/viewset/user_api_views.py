from rest_framework import viewsets, status, mixins 
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from user.models.user_model import UserModel
from api.serializers.user_serializer import UserSerializer
from api.serializers.password_serializer import ChangePasswordSerializer
from django.contrib.auth.hashers import make_password



class UserViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()
    
    
    # @action(detail= True, methods=['POST'])
    # def set_password(self, request, pk = None):
    #     user = self.get_object()
    #     serializer = UserSerializer(data = request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data.get('password'))
    #         user.save()
    #         Response = ({"status": "success"})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Action pour mettre à jour uniquement le mot de passe
    @action(detail=True, methods=['patch'], url_path='set-password')
    def set_password(self, request, pk=None):
        user = self.get_object()  # Récupère l'utilisateur par son ID
        data = request.data
        password = data.get('password')  # Récupère le mot de passe depuis la requête

        if not password:
            return Response({'error': 'Le mot de passe est requis'}, status=400)

        # Met à jour le mot de passe en le chiffrant
        user.password = make_password(password)
        user.save()

        return Response({'status': 'Mot de passe changer avec succès'}, status=200)

        
    @action(detail= False, methods=['post'])
    def create_user_with_crypt(self, request, pk = None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save(password=make_password(password))
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)  
    
    def get_object(self):
        return self.request.user 
    
    # @action(detail= True, methods=['put'], serializer_class = ChangePasswordSerializer)
    # def change_password (self, request, pk = None):
    #     user = request.user
    #     serializer = ChangePasswordSerializer(data = request.data,  )
        
    #     if serializer.is_valid():
    #         # Vérifier l'ancien mot de passe
    #         if not user.check_password(serializer.validated_data['password']):
    #             return Response({"detail": "L'ancien mot de passe est incorrect."}, status=status.HTTP_400_BAD_REQUEST)
            
    #         # Mettre à jour le mot de passe
    #         user.make_password(serializer.validated_data['new_password'])
    #         user.save()
    #         return Response({"status": "Mot de passe mis a jour"}, status=status.HTTP_200_OK)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# @csrf_exempt
# def user_api(request):
    
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer_class = UserSerializer(users, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    

# @csrf_exempt
# def user_api_view_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer_class = UserSerializer(users, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)
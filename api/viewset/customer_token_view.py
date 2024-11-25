from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class CustomerTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        #gerer les erreurs au token apres la validation
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        # Obtenir le token et instancier le user
        token = serializer.validated_data
        user = serializer.user
        
        #reponse en data de l'api user
        
        response_data = {
            'access': token['access'],
            'refresh': token['refresh'],
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'role': user.role.name if user.role else None
        }
        
        return Response(response_data)
        

       
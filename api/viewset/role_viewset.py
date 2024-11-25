from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from user.models.role_model import RoleModel
from api.serializers.role_serializer import RoleSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]


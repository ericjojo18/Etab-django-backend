from  rest_framework import viewsets, permissions, mixins
from school.models.school_model import SchoolModel
from api.serializers.school_serializer import SchoolSerializer


class SchoolViewSet(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        # Retourne le premier School (ou aucun)
        try:
            return SchoolModel.objects.first()
        except SchoolModel.DoesNotExist:
            return None

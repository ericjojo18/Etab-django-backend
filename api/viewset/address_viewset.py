from rest_framework import viewsets
from base.models.address_model import AddressModel
from api.serializers.address_serializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
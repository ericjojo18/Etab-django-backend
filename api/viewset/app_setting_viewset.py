from rest_framework import viewsets, mixins
from school.models.app_setting_model import AppSettingModel
from api.serializers.app_setting_serializer import AppSettingSerializer


class AppSettingViewSet(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = AppSettingModel.objects.all()
    serializer_class = AppSettingSerializer

    def get_object(self):
        # Retourne le premier AppSetting (ou aucun)
        try:
            return AppSettingModel.objects.first()
        except AppSettingModel.DoesNotExist:
            return None

from  rest_framework import serializers
from user.models.user_model import UserModel
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField( required=True,)
    new_password = serializers.CharField( required=True,validators=[validate_password])
    
    class Meta:
        model = UserModel
        fields = ["password", "new_password"]
    
    def validate_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError(
                "L'ancien mot de passe est incorrect. Please enter it again."
            )
        return value
    def validate_new_password(self, value):
        return value
    
    def update(self, instance, validated_data):
        user = instance
        user.set_password(validated_data['new_password'])
        user.save()
        return user
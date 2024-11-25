from rest_framework import serializers
from user.models.user_model import UserModel
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True, validators=[validate_password])
    # confirmed_password = serializers.CharField(write_only=True, required=True,)
    class Meta:
        model = UserModel
        fields = ["id","username","password","first_name","last_name", "email", "role", "school"]
        extra_kwargs = {'password': {'write_only': True}}
        
        
        # def validate(self, data):
            
            
        #         if data['password'] != data['confirmed_password']:
        #             raise serializers.ValidationError({'password': 'Les mots de passe doivent correspondre.'})
        #         return data
        
        def create(self, validated_data ):
            
            # Retirer le champ 'confirmed_password'
            
            
            role = validated_data.pop('role')
            school = validated_data.pop('school')
            user = UserModel.objects.create(**validated_data, role=role, school=school)
            user.make_password(validated_data['password'])
            user.roles.set(role)
            user.save()
            return user
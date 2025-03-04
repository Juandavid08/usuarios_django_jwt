from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nombre_completo', 'date_joined', 'is_active']
        read_only_fields = ['id', 'date_joined']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'nombre_completo', 'password', 'is_active']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Cifrar la contraseña
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)

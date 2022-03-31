from dataclasses import field
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import HWFUser

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login

User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
JWT_ALLOW_REFRESH = api_settings.JWT_ALLOW_REFRESH
JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER
JWT_PAYLOAD_GET_USER_ID_HANDLER = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = HWFUser.objects.create(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            profile_image = validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = HWFUser
        fields = ['nickname','name','email','password','profile_image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(write_only =True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email = email, password=password)
        if user is None:
            return {
                'email' : 'None'
            }
        
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                '잘못된 아이디 또는 패스워드 입니다.'
            )
        return {
            'email': user.email,
            'token':jwt_token
        }

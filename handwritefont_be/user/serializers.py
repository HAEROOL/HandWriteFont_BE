from dataclasses import field
from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
from .models import HWFUser

# class LoginSerializer(serializers.ModelSerializer):


class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = HWFUser.objects.create(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = HWFUser
        fields = ['nickname','name','email','password']

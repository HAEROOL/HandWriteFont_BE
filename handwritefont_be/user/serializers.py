# V1 Import list
from dataclasses import field
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import HWFUser

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
import jwt

# V2 Import list
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import HWFUser
from rest_framework.validators import UniqueValidator

# V2 User Serializer
class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image, nickname
    # profile_image = serializers.ImageField(use_url=True)
    nickname = serializers.CharField(max_length=50, allow_blank=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['profile_image'] = self.validated_data.get('profile_image', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

class UserSerializer(serializers.ModelSerializer):
    fonts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = HWFUser
        exclude = ['last_login','is_active','is_admin','is_superuser','groups','user_permissions','password']

class EmailUniqueCheckSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=HWFUser.objects.all())])

    class Meta:
        model = HWFUser
        fields = ['email']
        
class NicknameUniqueCheckSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True,min_length=1, max_length=50, validators=[UniqueValidator(queryset=HWFUser.objects.all())])

    class Meta:
        model = HWFUser
        fields = ['nickname']
# V1 User Serializer

# class UserCreateSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = HWFUser.objects.create(
#             email = validated_data['email'],
#             nickname = validated_data['nickname'],
#             name = validated_data['name'],
#             profile_image = validated_data['profile_image']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#     class Meta:
#         model = HWFUser
#         fields = ['nickname','name','email','password','profile_image']



# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=64)
#     password = serializers.CharField(write_only =True)
#     token = serializers.CharField(max_length=255, read_only=True)


#     def validate(self, data):
#         email = data['email']
#         password = data['password']
#         user = authenticate(email = email, password=password)
#         if user is None:
#             return {
#                 'email' : 'None'
#             }
        
#         try:
#             # jwt_token = jwt.encode(user, SECRET)
#             update_last_login(None, user)

#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 '잘못된 아이디 또는 패스워드 입니다.'
#             )
#         return {
#             'email': user.email,
#             'token':jwt_token
#         }

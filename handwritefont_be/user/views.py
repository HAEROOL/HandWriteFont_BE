# V1 Import List
# from rest_framework import generics
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAdminUser
# from .serializers import UserCreateSerializer, UserLoginSerializer,UserSerializer
# from .models import HWFUser
# V2 Import List
from rest_framework import generics
from .serializers import UserSerializer, EmailUniqueCheckSerializer, NicknameUniqueCheckSerializer
from .models import HWFUser
from main.models import Font
from rest_framework.response import Response
from rest_framework import status

# V2 User View

# 유저 디테일 페이지 데이터 GET, PUT, PATCH
class HWFUserDetail(generics.RetrieveUpdateAPIView):
    queryset = HWFUser.objects.all()
    serializer_class = UserSerializer

class EmailUniqueCheck(generics.CreateAPIView):
    serializer_class = EmailUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return Response(data={'detail':'You can use this email :)'}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = 'This email is alreay Used :('
            return Response(data=detail, status=status.HTTP_400_BAD_REQUEST)

class NickNameUniqueCheck(generics.CreateAPIView):
    serializer_class = NicknameUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return Response(data={'detail':'You can use this NickName :)'}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = 'This NickName is alreay Used :('
            return Response(data=detail, status=status.HTTP_400_BAD_REQUEST)
# V1 User View

# @permission_classes([IsAdminUser])
# class HWFUserListView(generics.ListAPIView):
#     queryset = HWFUser.objects.all()
#     serializer_class = UserSerializer
    
# class HWFUserView(generics.RetrieveAPIView):
#     queryset = HWFUser.objects.all()
#     serializer_class = UserSerializer

# # @permission_classes([AllowAny])
# # class HWFUserCreate(generics.CreateAPIView):
# #     queryset = HWFUser.objects.all()
# #     serializer_class = UserCreateSerializer

# # @api_view(['POST']) 
# # @permission_classes([AllowAny]) # 인증 필요없다
# # def signup(request):
# #     serializer = UserCreateSerializer(data=request.data) 
# #     if serializer.is_valid(raise_exception=True):
# #         serializer.save() # DB 저장
# #         return Response(serializer.data, status=201) 

# # @api_view(['POST'])
# # @permission_classes([AllowAny])
# # def signin(request):
# #     if request.method == "POST":
# #         serializer = UserLoginSerializer(data=request.data)

# #         if not serializer.is_valid(raise_exception=True):
# #             return Response({"message" : "잘못된 Data 값 입니다."}, status=status.HTTP_409_CONFLICT)
# #         if serializer.validated_data['email'] == 'None':
# #             return Response({"message" : "로그인에 실패하였습니다."}, status=status.HTTP_409_CONFLICT)
# #         response = {
# #             'success' : 'True',
# #             'token' : serializer.data['token']
# #         }
# #         return Response(response, status=status.HTTP_200_OK)
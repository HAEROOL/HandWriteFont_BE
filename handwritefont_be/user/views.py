from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import UserCreateSerializer, UserLoginSerializer,UserSerializer
from .models import HWFUser

@permission_classes([IsAdminUser])
class HWFUserListView(generics.ListAPIView):
    queryset = HWFUser.objects.all()
    serializer_class = UserSerializer
    
class HWFUserView(generics.RetrieveAPIView):
    queryset = HWFUser.objects.all()
    serializer_class = UserSerializer

# @permission_classes([AllowAny])
# class HWFUserCreate(generics.CreateAPIView):
#     queryset = HWFUser.objects.all()
#     serializer_class = UserCreateSerializer

@api_view(['POST']) 
@permission_classes([AllowAny]) # 인증 필요없다
def signup(request):
    serializer = UserCreateSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save() # DB 저장
        return Response(serializer.data, status=201) 

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == "POST":
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message" : "잘못된 Data 값 입니다."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == 'None':
            return Response({"message" : "로그인에 실패하였습니다."}, status=status.HTTP_409_CONFLICT)
        response = {
            'success' : 'True',
            'token' : serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
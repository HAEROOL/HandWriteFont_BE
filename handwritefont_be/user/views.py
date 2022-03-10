from .serializers import UserCreateSerializer
from .models import HWFUser
from rest_framework import generics

class HWUserCreate(generics.CreateAPIView):
    queryset = HWFUser.objects.all()
    serializer_class = UserCreateSerializer
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

from .models import Font
from .serializers import FontSerializer

# Create your views here.

@permission_classes([IsAuthenticatedOrReadOnly])
class FontListView(ListCreateAPIView):
    queryset = Font.objects.all().order_by('-created_date')
    serializer_class = FontSerializer

class FontView(RetrieveAPIView):
    queryset = Font.objects.all()
    serializer_class = FontSerializer


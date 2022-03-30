from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from .models import Font
from .serializers import FontSerializer

# Create your views here.
class FontListView(ListCreateAPIView):
    queryset = Font.objects.all().order_by('-created_date')
    serializer_class = FontSerializer

class FontView(RetrieveAPIView):
    queryset = Font.objects.all()
    serializer_class = FontSerializer


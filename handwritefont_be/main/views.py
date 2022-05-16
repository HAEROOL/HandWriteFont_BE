from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

from .models import Font
from .serializers import FontSerializer,FontLookAroundSerializer,FontPublicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@permission_classes([IsAuthenticatedOrReadOnly])
class FontListView(ListCreateAPIView):
    queryset = Font.objects.all().order_by('-created_date')
    serializer_class = FontSerializer

class FontView(RetrieveAPIView):
    queryset = Font.objects.all()
    serializer_class = FontSerializer

class FontView(RetrieveAPIView):
    queryset = Font.objects.all()
    serializer_class = FontPublicSerializer

@api_view(['GET'])
def fontview(request):
    queryset = Font.objects.filter(public=True)
    name = request.query_params.get('name')
    if name is not None:
        queryset = queryset.get(name=name, public=True)
        serializer = FontLookAroundSerializer(queryset, context={'request':request}).data
    else:
        serializer = FontLookAroundSerializer(queryset,many=True, context={'request':request}).data
    return Response(serializer)
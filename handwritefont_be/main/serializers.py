from rest_framework import serializers
from .models import Font

class FontSerializer(serializers.ModelSerializer):
    like_num = serializers.ReadOnlyField()
    class Meta:
        model = Font
        fields = '__all__'

class FontLookAroundSerializer(serializers.ModelSerializer):
    like_num = serializers.ReadOnlyField()
    class Meta:
        model = Font
        fields = ['like_num','name','file']
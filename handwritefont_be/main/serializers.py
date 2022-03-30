from dataclasses import field
from rest_framework import serializers
from .models import Font

class FontSerializer(serializers.ModelSerializer):
    like_num = serializers.ReadOnlyField()
    class Meta:
        model = Font
        fields = '__all__'
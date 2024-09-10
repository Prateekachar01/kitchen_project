from rest_framework import serializers
from .models import AddArea

class AddAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddArea
        fields='__all__'
from rest_framework import serializers
from .models import AddFood

class AddFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddFood
        fields='__all__'
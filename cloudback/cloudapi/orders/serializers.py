from rest_framework import serializers
from .models import AddOrder

class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddOrder
        fields='__all__'

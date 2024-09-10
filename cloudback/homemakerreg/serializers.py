from rest_framework import serializers
from .models import HomeMakerReg

class HomeMakerRegSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomeMakerReg
        fields='__all__'
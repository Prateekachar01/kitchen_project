from rest_framework import serializers
from .models import CloudAdmin

class CloudAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=CloudAdmin
        fields='__all__'
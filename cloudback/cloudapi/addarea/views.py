from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import AddArea
from .serializers import AddAreaSerializer

class AddAreaView(APIView):
    def post(self,request):
        serializer=AddAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

    def get(self,request):
        obj=AddArea.objects.all()
        serializer=AddAreaSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
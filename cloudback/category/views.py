from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer

class CategoryView(APIView):
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        obj=Category.objects.all()
        serializer=CategorySerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
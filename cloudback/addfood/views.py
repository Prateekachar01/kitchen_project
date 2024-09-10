from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import AddFood
from .serializers import AddFoodSerializer

class AddFoodView(APIView):
    def post(self,request):
        serializer=AddFoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        obj=AddFood.objects.all()
        serializer=AddFoodSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class FoodDetailsById(APIView):
    def get(self,request,userId):
        try:
            obj=AddFood.objects.filter(userId=userId)
        except AddFood.DoesNotExist:
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        serializer=AddFoodSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

 
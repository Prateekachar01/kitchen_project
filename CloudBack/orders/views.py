from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import AddOrder
from .serializers import AddOrderSerializer

class AddOrderView(APIView):

    def post(self,request):
        serializer=AddOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

    def get(self,request):
        obj=AddOrder.objects.all()
        serializer=AddOrderSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class OrderDetailsById(APIView):
    def get(self,request,userId):
        obj=AddOrder.objects.filter(userId=userId)
        if not obj.exists():  
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        serializer=AddOrderSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class OrderDetailsByKitchenId(APIView):
    def get(self,request,kitchenId):
        obj=AddOrder.objects.filter(kitchenId=kitchenId)
        if not obj.exists():  
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        serializer=AddOrderSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class OrderDeliver(APIView):
    def put(self,request,kitchenId,id):
        try:
            obj=AddOrder.objects.get(kitchenId=kitchenId,id=id)
        except AddOrder.DoesNotExist:
            message={"message":"Not Found"}  
            return Response(message,status=status.HTTP_404_NOT_FOUND)

        obj.status='Delivered'
        serializer=AddOrderSerializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
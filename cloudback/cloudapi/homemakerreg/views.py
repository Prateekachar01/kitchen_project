from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import HomeMakerReg
from .serializers import HomeMakerRegSerializer


class HomeMakerRegView(APIView):
     def post(self,requset):
        serializer=HomeMakerRegSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)     

     def get(self,request):
        obj=HomeMakerReg.objects.all()
        serializer=HomeMakerRegSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HomeMakerLoginView(APIView):
    queryset=HomeMakerReg.objects.all()
    serializer_class=HomeMakerRegSerializer

    def post(self,request):
        userId=request.data.get('userId')
        password=request.data.get('password')
        user=HomeMakerReg.objects.filter(userId=userId,password=password).first()

        if user:
            if user.status=='Approved':
                return Response({'message':'Login Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'message':'You are not approved'},status=status.HTTP_403_FORBIDDEN)
        
        else:
            return Response({'message':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)


class HomeMakerApproveView(APIView):
    def put(self,request,userId):
        try:
            obj=HomeMakerReg.objects.get(userId=userId)
        except HomeMakerReg.DoesNotExist:
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        obj.status='Approved'
        serializer=HomeMakerRegSerializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class NearyByMakers(APIView):
    def get(self, request, area):
        obj = HomeMakerReg.objects.filter(area=area,status='Approved')
          
        if not obj.exists():  
            message = {"message": "No nearby makers not found in the specified area"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
       
        serializer = HomeMakerRegSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserRegister
from .serializers import UserRegSerializer

class UserRegView(APIView):

    def get(self,request):
        obj=UserRegister.objects.all()
        serializer=UserRegSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,requset):
        serializer=UserRegSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)     
  

class UserLoginView(APIView):
    # queryset=UserRegister.objects.all()
    # serializer_class=UserRegSerializer

    def post(self,request):
        userId=request.data.get('userId')
        password=request.data.get('password')
        user=UserRegister.objects.filter(userId=userId,password=password).first()

        if user:
            return Response({'message':'Login Successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)


class UserById(APIView):
    def get(self,request,userId):
        try:
            obj=UserRegister.objects.get(userId=userId)
        except UserRegister.DoesNotExist:
            message={"message":"Not Found"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        serializer=UserRegSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class DeleteUser(APIView):
    def delete(self,request,userId):
        try:
            obj=UserRegister.objects.get(userId=userId)
            obj.delete()
            return Response({"message":"User Deleted Successfully"})
        except UserRegister.DoesNotExist:
            message=({"message":"User Not Found"})
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"messge":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CloudAdmin
from .serializers import CloudAdminSerializer
from rest_framework import status

class CloudAdminLoginView(APIView):
    queryset=CloudAdmin.objects.all()
    serializer_class=CloudAdminSerializer

    def post(self,request):
        userId=request.data.get('userId')
        password=request.data.get('password')
        user=CloudAdmin.objects.filter(userId=userId,password=password).first()

        if user:
            return Response({'message':'Login Successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)




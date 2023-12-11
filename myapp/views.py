from django.shortcuts import render 
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from .models import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import action
from drf_yasg import openapi 
# from .tasks import add
# result=add.delay(4,5)  

class profileView(APIView):
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(operation_description='Upload file',
        request_body=ProfileSerializer,
    responses={status.HTTP_201_CREATED:ProfileSerializer},
manual_parameters=[openapi.Parameter(name="file",in_=openapi.IN_FORM,type=openapi.TYPE_FILE,required=True,description="Document")])
    @action(detail=False, methods=['post'])
    
    def post(self,request):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'done'})
        return Response(serializer.errors)

    def get(self,request):
        data=Profile.objects.all()
        serializer=ProfileSerializer(data,many=True)
        return Response(serializer.data)
    

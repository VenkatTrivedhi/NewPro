from django.shortcuts import render
from .models import Message,User
from .serializers import MessageSerializer,UserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.throttling import UserRateThrottle
from rest_framework.authentication import TokenAuthentication




class MessagePostAPI(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]

    # overriding post method,such that created_by field will hold the 
    # user data who posted the message with authentication token
    
    def post(self, request, format=None):
    
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





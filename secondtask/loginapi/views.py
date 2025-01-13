from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny




# Create your views here.
class registerAPI(APIView):
    def post(self,request):
        data=request.data
        serialuser=registerSerializer(data=data)
        if serialuser.is_valid():
            serialuser.save()
            return Response(serialuser.data)
        return Response(serialuser.errors)
    
class loginAPI(APIView):
    def post(self,request):
        data=request.data
        serialuser=loginSerializer(data=data)

        print(data)
        if  serialuser.is_valid():
            username=serialuser.data['username']
            password=serialuser.data['password']
            userobj=authenticate(username=username,password=password)
            refresh=RefreshToken.for_user(userobj)
            return Response({
                "refresh":str(refresh),
                'access':str(refresh.access_token)
                })
       
        return Response(serialuser.errors)
    
class helloworld2(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        return Response("hello-world-two")
    
class helloworld1(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        return Response("hello-world-one")
    
class refreshTokenAPI(APIView):

    def post(self,request):
        refreshToken=request.data.get('refresh')
        try:
            newToken=RefreshToken(refreshToken)
            return Response({"access":str(newToken.access_token)})
        except Exception as e:
            return Response({'error':'token is expired'})

    


        
        



       


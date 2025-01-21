from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.cache import cache




# Create your views here.
class registerAPI(APIView):
    
    def get(self,request,id=None):
        if id:
            users = cache.get(f'getuser{id}')
            if users:
                print('from cache')
            else:
                print('from db')
                getid=User.objects.get(id=id)
            # user_queryset = User.objects.all()
                serialusers = registerSerializer(getid).data  

            
                cache.set(f'getuser{id}', serialusers, timeout=60)
                users = serialusers

            return Response(users)
        #no id then return list
        users = cache.get('userList')
        if users:
                print('from cache')
        else:
                print('from db')
                
                user_queryset = User.objects.all()
                serialusers = registerSerializer(user_queryset,many=True).data  

            
                cache.set('userList', serialusers, timeout=60)
                users = serialusers

        return Response(users)
        
    def post(self,request):
        data=request.data
        serialuser=registerSerializer(data=data)
        if serialuser.is_valid():
            serialuser.save()
            users = cache.get('userList')
            users.append(serialuser.data)
            cache.set('userList', users)
            return Response(serialuser.data)
        return Response(serialuser.errors)
    
            
    def put(self,request,id):
        data=request.data
        getid=User.objects.get(id=id)
        serialusers=registerSerializer(getid,data=data)
        if serialusers.is_valid():
            updatedUser=serialusers.save()

            serialupdateduser = registerSerializer(updatedUser).data
            #check for the user in cache
            
            users = cache.get('userList')
            for index, user_data in enumerate(users):
                if user_data['id'] == id:
                    users[index] = registerSerializer(updatedUser).data
                    cache.set('userList', users,timeout=60)
           
            
            return Response(serialusers.data)
       
        return Response(serialusers.errors)
        
        # if serialusers.is_valid():
        #     updatedUser=serialusers.save()
        #     cache.set(f"user{updatedUser.id}",updatedUser,timeout=60)
        #     cache.delete("userList")
        #     return Response(serialusers.data)
        # return Response(serialusers.errors)
    
    def delete(self,request,id):
        
        getid=User.objects.get(id=id)
        getid.delete()
        users = cache.get('userList')
        for index, user_data in enumerate(users):
            if user_data['id'] == id:
                del users[index]
                cache.set('userList', users,timeout=60)
        return Response({'message':'User deleted'})

        
    
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


        
    


        
        



       


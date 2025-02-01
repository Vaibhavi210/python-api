from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.cache import cache
from .services.implement import *
from enum import Enum
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
import requests
from rest_framework.exceptions import ValidationError
from .services.validation_service import *


class errorCodes(Enum):
    
    contactError={"error_code": "1003", "error_message": "Error while processing contact number & email"}
    usernotfound={"error_code": "1004", "error_message": "user not found"}




# Create your views here.
class registerAPI(APIView):
    
    def get(self,request,id=None):
        try:
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
        except ObjectDoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
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
            if users:
                users.append(serialuser.data)
                cache.set('userList', users)
                return Response(serialuser.data)
            else:
                return Response("your cache is empty")
        return Response(serialuser.errors)
    
            
    def put(self,request,id):
        try:
            data=request.data
            getid=User.objects.get(id=id)
            serialusers=registerSerializer(getid,data=data)
            if serialusers.is_valid():
                updatedUser=serialusers.save()

                serialupdateduser = registerSerializer(updatedUser).data
                #check for the user in cache
                
                users = cache.get('userList')
                if users:
                    for index, user_data in enumerate(users):
                        if user_data['id'] == id:
                            users[index] = registerSerializer(updatedUser).data
                            cache.set('userList', users,timeout=60)
                
                    
                    return Response(serialusers.data)
                else:
                    return Response("your cache is empty")
        except ObjectDoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(serialusers.errors)
        
       
    
    def delete(self,request,id):
        try:
            getid=User.objects.get(id=id)
            getid.delete()
            users = cache.get('userList')
            if users:
                for index, user_data in enumerate(users):
                    if user_data['id'] == id:
                        del users[index]
                        cache.set('userList', users,timeout=60)
            else:
                    return Response("your cache is empty")
            return Response({'message':'User deleted'})
        except ObjectDoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        
    
class loginAPI(APIView):
    def post(self,request):
        data=request.data
        serialuser=loginSerializer(data=data)

        print(data)
        if  serialuser.is_valid():
            username=serialuser.data['username']
            password=serialuser.data['password']
            userobj=authenticate(username=username,password=password)
            if userobj:
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
        
class emailandPhone(APIView):
    def post(self,request):
        
        data=request.data
        serialdata=customerSerializer(data=data)
      
        try:
            if serialdata.is_valid():
                email=serialdata.validated_data['email']
                email_implement = emailandPhoneImplement()
                email_implement.validationForEmail(email)
        except ValidationError as ve:
            return Response({'error':str(ve)},status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            contactNo=serialdata.validated_data['contactNo']
                    
            contact_implement=emailandPhoneImplement()
            contact_implement.validationForPhone(contactNo)
        except ValidationError as ve:
            return Response({'error':str(ve)},status=status.HTTP_406_NOT_ACCEPTABLE)
             
                
        except Exception as e:
                    return Response(serialdata.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Your email & phone number are validated successfully")  
    
            
            
@api_view(['GET','POST'])
def success(request):
     url="http://127.0.0.1:5000/"
     if request.method=='GET':
          response=requests.get(url+"success")
     elif  request.method=='POST':
               data=request.data
               response=requests.post(url+"post/success",json=data)
     return Response(response.json(), status=response.status_code) 

@api_view(['GET'])
def frobidden(request):
     url="http://127.0.0.1:5000/"
     
     response=requests.get(url+"forbidden")
     return Response(response.json(), status=response.status_code)

@api_view(['POST'])
def badrequest(request):
     data=request.data
     url="http://127.0.0.1:5000/"
     
     response=requests.post(url+"badrequest",json=data)
     return Response(response.json(), status=response.status_code)

@api_view(['POST'])
def snapchat(request,ad_account_id):
     data=request.data
     url=f"http://127.0.0.1:5000/v1/adaccounts/{ad_account_id}s/segments"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)

@api_view(['POST'])
def tiktok(request):
     data=request.data
     url="http://127.0.0.1:5000/open_api/v1.3/custom_audience/create/"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)

@api_view(['POST'])
def reddit(request,ad_account_id):
     data=request.data
     url=f"http://127.0.0.1:5000/api/v3/ad_accounts/{ad_account_id}/custom_audiences"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)


@api_view(['POST'])
def amazon(request):
     data=request.data
     url="http://127.0.0.1:5000/v2/dp/audiencemetadata/"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)


@api_view(['POST'])
def yahoo(request):
     data=request.data
     url="http://127.0.0.1:5000/traffic/audiences/email_address/"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)


@api_view(['POST'])
def meta(request,AD_ACCOUNT_ID):
     data=request.data
     url=f"http://127.0.0.1:5000/v18.0/{AD_ACCOUNT_ID}/customaudiences"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)



@api_view(['POST'])
def linkedin(request,adAccountId):
     data=request.data
     url=f"http://127.0.0.1:5000/v2/adAccounts/{adAccountId}/audiences"
     
     response=requests.post(url,json=data)
     return Response(response.json(), status=response.status_code)


class emailandPhoneusingPydentic(APIView):
    def post(self,request):
        try:
            data=request.data
            serialdata=customerSerializer(data=data)
            if serialdata.is_valid():
                validate_data=validInput(email=serialdata.data['email'],contactNo=serialdata.data['contactNo'])
                return Response(validate_data)
        except Exception as e:
                    return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serialdata.errors)

class phoneValidation(APIView):
     @validPhone
     def post(self,request):
          data=request.data 
          serialdata=customerSerializer(data=data)
          if serialdata.is_valid():
               return Response(serialdata.data)
          return Response(serialdata.errors)
               



   
     
       
        



        
    


        
        



       


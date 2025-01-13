from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
# Create your views here.
@api_view(["GET"])
def helloworld(request):
    return Response({"message":"Hello World"})

@api_view(['GET'])
def getalluser(request):
    users=user.objects.all()
    serialuser=userSerializer(users,many=True)
    return Response({"data":serialuser.data})

@api_view(['GET'])
def getuser(request,id):
    users=user.objects.get(id=id)
    serialuser=userSerializer(users,many=False)
    return Response({"data":serialuser.data})

@api_view(['POST'])
def createuser(request):
    serialuser=userSerializer(data=request.data)
    
    if serialuser.is_valid():
        serialuser.save()
        return Response({"data":serialuser.data})

    return Response(serialuser.errors)

@api_view(['PUT'])
def updateusers(request,id):
    users=user.objects.get(id=id)
    serialuser=userSerializer(users,data=request.data)
    if serialuser.is_valid():
        serialuser.save()
        return Response({"data":serialuser.data})
    return Response(serialuser.errors)



@api_view(['DELETE'])
def deleteuser(request,id):
    users=user.objects.get(id=id)
    users.delete()
    return Response("user deleted successfully")

class crudSubject(APIView):
    def get(self,request):
        subjects=subject.objects.all()
        serialsubject=subjectSerializer(subjects,many=True)
        return Response(serialsubject.data)
    
    # def get(self,request):
    #     data=request.data
    #     subjects=subject.objects.get(id=data['id'])
    #     serialsubject=subjectSerializer(subjects,many=False)
    #     return Response(serialsubject.data)
    def post(self,request):
        data=request.data
        serialsubject=subjectSerializer(data=data)
        if serialsubject.is_valid():
            serialsubject.save()
            return Response(serialsubject.data)

        return Response(serialsubject.errors)
    def patch(self,request):
        data=request.data
        subjects=subject.objects.get(id=data['id'])
        serialsubject=subjectSerializer(subjects,data=data)
        if serialsubject.is_valid():
            serialsubject.save()
            return Response(serialsubject.data)
        return(serialsubject.errors)
    def delete(self,request):
        data=request.data
        getid=subject.objects.get(id=data['id'])
        getid.delete()
        return Response({"message":"data deleted"})
    

class crudMarks(APIView):
    def get(self,request):
        getmarks=marks.objects.all()
        serialmarks=marksSerializer(getmarks,many=True)
        return Response(serialmarks.data)
    
    def post(self,request):
        data=request.data
        serialmarks=marksSerializer(data=data)
        if serialmarks.is_valid():
            serialmarks.save()
            return Response(serialmarks.data)
        return Response(serialmarks.errors)

    def patch(self,request):
        data=request.data
        getid=marks.objects.get(id=data['id'])
        serialmarks=marksSerializer(getid,data=data)
        if serialmarks.is_valid():
            serialmarks.save()
            return Response(serialmarks.data)
        return Response(serialmarks.errors)
    
    def delete(self, request):
        data=request.data
        getid=marks.objects.get(id=data["id"])
        getid.delete()
        return Response({"msg":"data deleted"})


    
    










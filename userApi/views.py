from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token


# Create your views here.
# CREATE
class RegisterAPIView(APIView):
    serializer_class = StudentDetailsSerializer
    
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            # email = serializer.validated_data['email']
            serializer.save()
            user = User.objects.create_user(username=name)
            token,created = Token.objects.get_or_create(user=user)
            return Response({'user data': serializer.data,'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET
class StudentAPIView(APIView):
    serializer_class = StudentDetailsSerializer
    def get(self,request):
        data = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(data, many=True)
        return Response(serializer.data)

# PUT    
class EditAPIView(APIView):
    serializer_class = StudentDetailsSerializer
    def get(self,request,pk):
        if StudentDetails.objects.filter(pk=pk):
            data = StudentDetails.objects.get(pk=pk)
            serializer = StudentDetailsSerializer(data)
            return Response(serializer.data)
        else:
            return Response({"status':'Id Doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk):
        if StudentDetails.objects.filter(pk=pk):
            user = StudentDetails.objects.get(pk=pk)
            userData = StudentDetailsSerializer(instance=user,data=request.data)
            if userData.is_valid():
                userData.save()
                return Response({'Data':userData.data, 'Status':"Successfully Edited!!"})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status':'Id Doesn't exist"},status=status.HTTP_404_NOT_FOUND)
        
# DELETE
class DeleteAPIView(APIView):
    serializer_class = StudentDetailsSerializer
    def get(self,request,pk):
        if StudentDetails.objects.filter(pk=pk):
            data = StudentDetails.objects.get(pk=pk)
            serializer = StudentDetailsSerializer(data)
            return Response(serializer.data)
        else:
            return Response({"status':'Id Doesn't exist"},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if StudentDetails.objects.filter(pk=pk):
            user = StudentDetails.objects.get(pk=pk)
            user.delete()
            return Response({'status': 'Successfully Deleted!!'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"status':'Id Doesn't exist"},status=status.HTTP_404_NOT_FOUND)

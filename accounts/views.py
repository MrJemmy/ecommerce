from django.contrib.auth import authenticate, login, logout
from .models import User

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserLogoutSerializer


class UserDataAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer


class UserRegisterAPI(APIView):
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(): # raise_exception=True
            serializer.save()
            return Response({'msg' : 'Registration Success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():  # raise_exception=True
            user = authenticate(request, username=serializer.data['email'], password=serializer.data['password'])
            if user is not None:
                login(request, user)
                return Response({'msg': f'{user} is logged in successfully'}, status=status.HTTP_200_OK)
            return Response({'msg': 'invalid email of password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            logout(request)
            return Response({'info':'User is logged out'})
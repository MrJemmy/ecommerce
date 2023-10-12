from django.contrib.auth import authenticate, logout

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserRegisterSerializer, UserLoginSerializer, UserLogoutSerializer, UserProfileSerializer,
    UserChangePasswordSerializer, ResetPasswordSerializer
)
from .renderers import UserRenderers
from .utils import get_token_and_login


class UserDataAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer


class UserRegisterAPI(APIView):
    renderer_classes = [UserRenderers]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():  # raise_exception=True
            user = serializer.save()
            token = get_token_and_login(request, user)
            return Response({
                'msg': f'{user} registration and login success',
                'token': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    renderer_classes = [UserRenderers]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():  # raise_exception=True
            user = authenticate(request, username=serializer.validated_data['email'],
                                password=serializer.validated_data['password'])
            if user is not None:
                token = get_token_and_login(request, user)
                return Response({
                    'msg': f'{user} is logged in successfully',
                    'token': token
                }, status=status.HTTP_200_OK)
            return Response({'msg': 'invalid email or password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPI(APIView):
    renderer_classes = [UserRenderers]

    def post(self, request, *args, **kwargs):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            logout(request)
            return Response({'info': 'User is logged out'})


class UserProfileAPI(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordAPI(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'password change successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserResetPasswordAPI(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data, context={'user': request.user})

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response

from .serializers import RegisterSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        return Response({'user' : serializer.data})


class LoginAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is None:
            return Response({'info': 'invalid username or password'})
        login(request, user)
        return Response({'info': f'{user} is logged in'})


class LogoutAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, *args, **kwargs):
        user = self.get_serializer(User.objects.get())
        # if serializer.is_valid(raise_exception=True):
        if request.user.username == '':
            return Response({'info': 'user is not logged in'})
        logout(request)
        return Response({'info': f'{request.user.username} is logged out'})
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login


def get_token_and_login(request, user):
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
    login(request, user)
    return token

import os

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['body'],
            from_email='my_email@email.com',
            to=[data['user_email']]
        )
        email.send()

def get_token_and_login(request, user):
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
    login(request, user)
    return token



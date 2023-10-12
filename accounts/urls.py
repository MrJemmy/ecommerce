from django.urls import path
from .views import (UserRegisterAPI, UserLoginAPI, UserLogoutAPI, UserDataAPI, UserProfileAPI, UserChangePasswordAPI,
                    SendResetPasswordLinkAPI, UserResetPasswordAPI)

urlpatterns = [
    path('', UserDataAPI.as_view()),
    path('register/', UserRegisterAPI.as_view()),
    path('login/', UserLoginAPI.as_view()),
    path('logout/', UserLogoutAPI.as_view()),
    path('profile/', UserProfileAPI.as_view()),
    path('change-password/', UserChangePasswordAPI.as_view()),
    path('send-reset-password-link/', SendResetPasswordLinkAPI.as_view()),
    path('reset-password/<uid>/<token>/', UserResetPasswordAPI.as_view()),
]
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from .views import (UserRegisterAPI, UserLoginAPI, UserLogoutAPI, UserProfileAPI, UserChangePasswordAPI,
                    SendResetPasswordLinkAPI, UserResetPasswordAPI)

urlpatterns = [
    path('register/', UserRegisterAPI.as_view()),
    path('login/', UserLoginAPI.as_view()),
    path('logout/', UserLogoutAPI.as_view()),
    path('profile/', UserProfileAPI.as_view()),
    path('change-password/', UserChangePasswordAPI.as_view()),
    path('send-reset-password-link/', SendResetPasswordLinkAPI.as_view()),
    path('reset-password/<uid>/<token>/', UserResetPasswordAPI.as_view()),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
from django.urls import path
from .views import UserRegisterAPI, UserLoginAPI, UserLogoutAPI, UserDataAPI, UserProfileAPI

urlpatterns = [
    path('', UserDataAPI.as_view()),
    path('register/', UserRegisterAPI.as_view()),
    path('login/', UserLoginAPI.as_view()),
    path('logout/', UserLogoutAPI.as_view()),
    path('profile/', UserProfileAPI.as_view())
]
from django.urls import path
from .views import inti_store, ProductListAPI


urlpatterns = [
    path('', inti_store),
    path('list/', ProductListAPI.as_view()),
]

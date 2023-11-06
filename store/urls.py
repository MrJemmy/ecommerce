from django.urls import path, include
from .views import inti_store, ProductListAPI, ProductCrudAPI

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('view_set', ProductCrudAPI, basename='product')

urlpatterns = [
    path('', inti_store),
    path('list/', ProductListAPI.as_view()),
    path('product/', include(router.urls)),
]

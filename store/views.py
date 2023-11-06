from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions

from .serializers import ProductSerializer

from .models import Product

from .permissions import SellerGroupPermissions

from .mixins import GeneralMixinQuerySet

@api_view(['GET'])
def inti_store(request, *args, **kwargs):
    return Response({"msg": "init store"})


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ProductCrudAPI(GeneralMixinQuerySet, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [SellerGroupPermissions]
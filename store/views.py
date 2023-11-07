from rest_framework import generics, viewsets

from .serializers import ProductSerializer
from .models import Product
from .permissions import SellerGroupPermissions
from .mixins import GeneralMixinQuerySet

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCrudAPI(viewsets.ModelViewSet):
    """
    Use mixins "GeneralMixinQuerySet" before API View
    """
    serializer_class = ProductSerializer
    permission_classes = [SellerGroupPermissions]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
        # return Product.objects.all()
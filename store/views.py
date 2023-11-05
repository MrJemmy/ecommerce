from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .serializers import ProductSerializer

from .models import Product


@api_view(['GET'])
def inti_store(request, *args, **kwargs):
    return Response({"msg": "init store"})


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.is_valid(raise_exception=True)
        serializer.save()

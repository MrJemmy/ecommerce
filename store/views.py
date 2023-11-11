from rest_framework import generics, viewsets

# from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer
from .models import Product
from .permissions import SellerGroupPermissions
# from .mixins import GeneralMixinQuerySet

from ecommerce.filter import SearchFilterNew


class ProductListAPI(generics.ListAPIView):
    # queryset = Product.objects.prefetch_related('user') # Run 2nd query to get others data.
    queryset = Product.objects \
        .only('name', 'price', 'user__email', 'user__first_name', 'user__last_name') \
        .select_related('user') # Join Tables.
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilterNew]
    filterset_fields = ['name']  # ?name=Product1 01 to search # foreign key need to pass ID
    search_fields = ['^name']  # ?search=Product2 to search  # not able ro find data with space why??
    ordering_fields = ['name']

    # def list(self, request, *args, **kwargs):
    #     print(dir(request))
    #     print(request.data)
    #     print(request.query_params)
    #     return super().list(request, *args, **kwargs)


class ProductCrudAPI(viewsets.ModelViewSet):
    """
    Use mixins "GeneralMixinQuerySet" before API View
    """
    serializer_class = ProductSerializer
    permission_classes = [SellerGroupPermissions]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
        # return Product.objects.all()
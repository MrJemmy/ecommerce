from .models import Product


class GeneralMixinQuerySet():

    def get_queryset(self, *args, **kwargs):
        print("==================")
        return Product.objects.filter(user=self.request.user)[0:2]
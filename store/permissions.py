from rest_framework import permissions


class SellerGroupPermissions(permissions.DjangoModelPermissions):  # , permissions.DjangoObjectPermissions

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        # 'OPTIONS': [],
        # 'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }



    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     # print(user.groups)
    #     # if user.groups == 'seller':
    #     #     return True
    #     if user.has_perm("store.add_product"):
    #         return True
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.user == request.user
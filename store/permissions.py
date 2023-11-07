from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class SellerGroupPermissions(permissions.DjangoModelPermissions):  # , permissions.DjangoObjectPermissions

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],  # customized with 'view_' for GET method
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
    #     # if user.groups == 'seller':  # user.groups returns None How can we check groups.
    #     #     return True
    #     if user.has_perm("store.add_product"):
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        """
        when in query_set we are getting all users data
        in that case this object permission will help full
        otherwise it will give that data not found error.
        """
        if obj.user == request.user:
            return True
        return False
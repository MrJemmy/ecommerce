from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "first_name", "last_name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "phone_no"]}),
        ("Permissions", {"fields": ["is_admin", "groups"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            "Add User",
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "phone_no", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "id", "first_name", "last_name", "phone_no"]
    ordering = ["email", "id"]
    filter_horizontal = ['groups']


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# # ... and, since we're not using Django's built-in permissions,
# # unregister the Group model from admin.
# admin.site.unregister(Group)

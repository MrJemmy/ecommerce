from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin
from .manager import UserManager
from django_enum import EnumField


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone_no = models.PositiveIntegerField(null=True, blank=True)  # Phone Number Regex Implementation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

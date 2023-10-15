from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from .manager import UserManager

class User(AbstractBaseUser):

    class UserType(models.IntegerChoices):
        ADMIN = 0
        BUYER = 1
        SELLER = 2

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    phone_no = models.PositiveIntegerField(null=True, blank=True)
    type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.BUYER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

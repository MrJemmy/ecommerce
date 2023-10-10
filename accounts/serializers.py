from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_date):
    #     user = User.objects.create_user(
    #         username=validated_date['username'], email=validated_date['email'], password=validated_date['password'])
    #     return user

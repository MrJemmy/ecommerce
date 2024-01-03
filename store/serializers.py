from rest_framework import serializers
from .models import Product
from accounts.serializers import UserRegisterSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = UserRegisterSerializer(source='user', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'seller'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        print(self.context.get('request').user)
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

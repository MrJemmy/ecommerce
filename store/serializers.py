from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        print(self.context.get('request').user)
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


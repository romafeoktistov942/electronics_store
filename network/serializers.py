from rest_framework import serializers

from .models import NetworkNode, Product


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "debt",
            "created_at",
        ]
        read_only_fields = ["debt"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

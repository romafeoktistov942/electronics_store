from rest_framework import serializers

from .models import NetworkNode, Product


class NetworkNodeSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(source="level", read_only=True)
    level_display = serializers.CharField(
        source="level_display", read_only=True
    )

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
            "level",
            "level_display",
        ]
        read_only_fields = ["debt"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "model", "release_date", "network_node"]

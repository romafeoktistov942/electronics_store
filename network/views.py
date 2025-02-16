from rest_framework import viewsets
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer
from rest_framework import filters
from users.permissions import IsActiveStaff


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["country"]
    permission_classes = [IsActiveStaff]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveStaff]

from rest_framework import filters, viewsets

from users.permissions import IsActiveStaff

from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


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

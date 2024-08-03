from rest_framework import viewsets
from .models import  Product, ProductCategory, ProductImage
from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer
from .permissions import IsAdminOrGetOnly

class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrGetOnly, ]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrGetOnly, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrGetOnly, ]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
from rest_framework import routers  

from .viewsets import ProductCategoryViewSet, ProductViewSet, ProductImageViewSet

app_name = 'product'

router = routers.DefaultRouter()
router.register('product-category', ProductCategoryViewSet)
router.register('product', ProductViewSet)
router.register('product-image', ProductImageViewSet)

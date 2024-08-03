from rest_framework import routers
from .viewsets import OrderViewSet, OrderItemViewSet

app_name = 'order'

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'order-item', OrderItemViewSet)
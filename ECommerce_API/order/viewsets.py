from rest_framework import viewsets, mixins
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from .permissions import IsOwnerOrStaffOrNone, IsAllowedToViewOrderItems

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrStaffOrNone, ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToViewOrderItems, ]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


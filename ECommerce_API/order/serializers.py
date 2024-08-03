from rest_framework import serializers
from product.models import Product
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product')
    product = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='product-detail')

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product', 'price', 'quantity', ]

class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(source='order_items', many=True, write_only=True)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'created_on', 'updated_on', 'paid', 'total_price', 'items']
        read_only_fields = ['created_on', 'updated_on', 'paid', 'total_price', 'user']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user.profile  
        order = Order.objects.create(user=user, **validated_data)

        total_price = 0
        for item_data in items_data:
            item_data['order'] = order
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price
            total_price += price * quantity
            OrderItem.objects.create(**item_data)

        order.total_price = total_price
        order.save()

        return order

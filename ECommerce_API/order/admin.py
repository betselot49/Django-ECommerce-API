from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_on', 'updated_on', 'paid', 'total_price')
    list_filter = ('paid', 'created_on', 'updated_on')
    search_fields = ('user', 'paid')
    date_hierarchy = 'created_on'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    list_filter = ('order', 'product')
    search_fields = ('order', 'product')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

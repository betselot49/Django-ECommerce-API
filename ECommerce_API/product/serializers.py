from rest_framework import serializers

from .models import Product, ProductCategory, ProductImage

class ProductCategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')

    class Meta:
        model = ProductCategory
        fields = ['url', 'id', 'name', 'description', 'created_on', 'updated_on', 'slug', 'products']
        read_only_fields = ['created_on', 'updated_on']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['url', 'id', 'product', 'image', 'alt_text', 'created_on', 'updated_on']
        read_only_fields = ['created_on', 'updated_on']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=ProductCategory.objects.all(), slug_field='slug')
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'description', 'price', 'stock', 'available', 'created_on', 'updated_on', 'category', 'images']
        read_only_fields = ['created_on', 'updated_on', 'images']

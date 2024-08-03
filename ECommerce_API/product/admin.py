from django.contrib import admin

from .models import Product, ProductCategory, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created_on', 'updated_on')
    list_filter = ('available', 'created_on', 'updated_on')
    search_fields = ('name', 'description')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on', 'updated_on')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text', 'created_on', 'updated_on')
    search_fields = ('product', 'alt_text')



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
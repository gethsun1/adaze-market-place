from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'seller', 'id')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'description')
    ordering = ('name',)

from django.db import models
from users.models import CustomUser

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('children', 'Children'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('unisex', 'Unisex'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    images = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
        ('transporter', 'Transporter'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Updated related_name to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # Updated related_name to avoid conflicts
        blank=True
    )

    def __str__(self):
        return self.username

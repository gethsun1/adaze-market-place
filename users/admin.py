# adaze_marketplace/users/admin.py

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Display these fields in the user list page
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
    
    # Allow filtering by role, active status, and staff status
    list_filter = ('role', 'is_active', 'is_staff')
    
    # Enable searching by username and email
    search_fields = ('username', 'email')
    
    # Specify the default ordering of users (e.g., by date joined)
    ordering = ('date_joined',)
    
    # Optional: Add inline editing or customization
    # You can add more options or even fieldsets if you want to control which fields to show on the form
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Optionally, you can add extra settings like readonly_fields or specific help texts if needed

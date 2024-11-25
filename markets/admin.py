from django.contrib import admin
from .models import Market

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'description')
    search_fields = ('name', 'location')
    ordering = ('name',)

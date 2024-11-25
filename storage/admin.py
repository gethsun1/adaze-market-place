from django.contrib import admin
from .models import Storage

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'market', 'location', 'capacity', 'contact_details')
    list_filter = ('market',)
    search_fields = ('location', 'market__name')
    ordering = ('location',)

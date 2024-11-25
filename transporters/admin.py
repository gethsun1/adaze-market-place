from django.contrib import admin
from .models import Transporter

@admin.register(Transporter)
class TransporterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vehicle_type', 'payment_details')
    search_fields = ('user__username', 'vehicle_type')
    ordering = ('user',)

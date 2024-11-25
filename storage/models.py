from django.db import models
from markets.models import Market

class Storage(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='storages')
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(help_text="Capacity in number of items")
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return f"Storage at {self.location} ({self.market.name})"

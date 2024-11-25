from django.db import models
from users.models import CustomUser

class Transporter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='transporter_profile')
    vehicle_type = models.CharField(max_length=50)
    tracking_info = models.TextField(null=True, blank=True)
    payment_details = models.CharField(max_length=255)

    def __str__(self):
        return f"Transporter {self.user.username}"

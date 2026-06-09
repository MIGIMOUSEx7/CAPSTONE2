from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WholesalerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wholesaler_profile')
    stall_number = models.CharField(max_length=50)
    market_location = models.CharField(max_length=255, default="Bulua WBIT Terminal")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Stall {self.stall_number}"

class IoTNode(models.Model):
    wholesaler = models.ForeignKey(WholesalerProfile, on_delete=models.CASCADE, related_name='nodes')
    device_token = models.CharField(max_length=255, unique=True)
    stall_location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    battery_level = models.IntegerField(default=100)

    def __str__(self):
        return f"Node {self.id} ({self.stall_location})"

class CropBatch(models.Model):
    CROP_CHOICES = [
        ('EGGPLANT', 'Eggplant'),
        ('CUCUMBER', 'Cucumber'),
        ('CARROT', 'Carrot'),
    ]
    STATUS_CHOICES = [
        ('GREEN', 'Fresh'),
        ('AMBER', 'At-Risk'),
        ('RED', 'Spoiled'),
    ]
    
    wholesaler = models.ForeignKey(WholesalerProfile, on_delete=models.CASCADE, related_name='batches')
    iot_node = models.ForeignKey(IoTNode, on_delete=models.SET_NULL, null=True, blank=True)
    crop_type = models.CharField(max_length=20, choices=CROP_CHOICES)
    quantity_kg = models.DecimalField(max_digits=6, decimal_places=2)
    freshness_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='GREEN')
    predicted_shelf_life = models.DecimalField(max_digits=5, decimal_places=2, default=5.0) 
    arrival_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.crop_type} Batch #{self.id} ({self.freshness_status})"

class SensorLog(models.Model):
    iot_node = models.ForeignKey(IoTNode, on_delete=models.CASCADE, related_name='logs')
    crop_batch = models.ForeignKey(CropBatch, on_delete=models.CASCADE, related_name='sensor_logs', null=True, blank=True)
    temperature_c = models.DecimalField(max_digits=4, decimal_places=2)
    humidity_rh = models.DecimalField(max_digits=4, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Log {self.id} - Node {self.iot_node.id} at {self.timestamp}"
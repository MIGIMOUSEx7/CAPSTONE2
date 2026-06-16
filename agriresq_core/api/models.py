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
    # Core relationships kept intact
    wholesaler = models.ForeignKey(WholesalerProfile, on_delete=models.CASCADE, related_name='batches', null=True, blank=True)
    iot_node = models.ForeignKey(IoTNode, on_delete=models.SET_NULL, null=True, blank=True)
    
    # UI-specific fields tailored for React frontend
    batch_id = models.CharField(max_length=50, unique=True) # e.g. #001
    node = models.CharField(max_length=150) # e.g. Stall 1 • Node 01
    icon = models.CharField(max_length=10) # e.g. 🍆
    crop = models.CharField(max_length=100)
    scientific = models.CharField(max_length=150)
    qty = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    arrival = models.CharField(max_length=100)
    days = models.IntegerField(default=0) # Stored as a number
    daysColor = models.CharField(max_length=100) # Tailwind class
    temp = models.CharField(max_length=50)
    rh = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    statusBg = models.CharField(max_length=100) # Tailwind class for Batches page
    statusColor = models.CharField(max_length=100, blank=True, null=True) # Tailwind class for Dashboard

    def __str__(self):
        return f"{self.batch_id} - {self.crop}"

class SensorLog(models.Model):
    iot_node = models.ForeignKey(IoTNode, on_delete=models.CASCADE, related_name='logs')
    crop_batch = models.ForeignKey(CropBatch, on_delete=models.CASCADE, related_name='sensor_logs', null=True, blank=True)
    temperature_c = models.DecimalField(max_digits=4, decimal_places=2)
    humidity_rh = models.DecimalField(max_digits=4, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Log {self.id} - Node {self.iot_node.id} at {self.timestamp}"
    
class Listing(models.Model):
    crop = models.CharField(max_length=100)
    icon = models.CharField(max_length=10) # e.g. 🍆
    batch = models.CharField(max_length=50)
    vendor = models.CharField(max_length=200)
    status = models.CharField(max_length=50) # e.g. At-Risk
    statusBg = models.CharField(max_length=100) # Tailwind classes
    qty = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    temp = models.CharField(max_length=50)
    rh = models.CharField(max_length=50)
    priceType = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    inquiries = models.CharField(max_length=100)
    isAtRisk = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.crop} - {self.batch}"

class Transaction(models.Model):
    txn_id = models.CharField(max_length=50, unique=True) # e.g. #TXN-041
    buyerName = models.CharField(max_length=150)
    buyerRole = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    qty = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    typeBg = models.CharField(max_length=100)
    typeDot = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    statusBg = models.CharField(max_length=100)
    statusDot = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.txn_id} - {self.buyerName}"
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import WholesalerProfile, IoTNode, CropBatch, SensorLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class WholesalerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = WholesalerProfile
        fields = '__all__'

class IoTNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTNode
        fields = '__all__'

class CropBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropBatch
        fields = '__all__'

class SensorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorLog
        fields = '__all__'
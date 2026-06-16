from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    WholesalerProfile, 
    IoTNode, 
    CropBatch, 
    SensorLog,
    Listing, 
    Transaction
)

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
    # This maps the database 'batch_id' to the 'id' field React wants
    id = serializers.CharField(source='batch_id', read_only=True)

    class Meta:
        model = CropBatch
        fields = [
            'id', 'node', 'icon', 'crop', 'scientific', 'qty', 'price', 
            'arrival', 'days', 'daysColor', 'temp', 'rh', 'status', 
            'statusBg', 'statusColor'
        ]

class SensorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorLog
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    # Map Django's 'txn_id' to React's 'id' requirement
    id = serializers.CharField(source='txn_id', read_only=True)
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'buyerName', 'buyerRole', 'crop', 'batch', 'qty', 
            'total', 'type', 'typeBg', 'typeDot', 'status', 'statusBg', 
            'statusDot', 'time'
        ]
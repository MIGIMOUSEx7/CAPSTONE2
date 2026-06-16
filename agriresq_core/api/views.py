from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    WholesalerProfile, 
    IoTNode, 
    CropBatch, 
    SensorLog,
    Listing,
    Transaction
)
from .serializers import (
    WholesalerProfileSerializer, 
    IoTNodeSerializer, 
    CropBatchSerializer, 
    SensorLogSerializer,
    ListingSerializer,
    TransactionSerializer
)

# --- EXISTING CORE VIEWSETS ---

class WholesalerProfileViewSet(viewsets.ModelViewSet):
    queryset = WholesalerProfile.objects.all()
    serializer_class = WholesalerProfileSerializer
    # We will add authentication later, keeping it open for testing right now

class IoTNodeViewSet(viewsets.ModelViewSet):
    queryset = IoTNode.objects.all()
    serializer_class = IoTNodeSerializer

class CropBatchViewSet(viewsets.ModelViewSet):
    queryset = CropBatch.objects.all()
    serializer_class = CropBatchSerializer

class SensorLogViewSet(viewsets.ModelViewSet):
    queryset = SensorLog.objects.all()
    serializer_class = SensorLogSerializer

# --- NEW MARKETPLACE VIEWSETS ---

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-id') # Show newest first
    serializer_class = TransactionSerializer
from django.contrib import admin
from .models import (
    WholesalerProfile,
    IoTNode,
    CropBatch,
    SensorLog,
    Listing,
    Transaction
)

# Registering models so they appear in the Django Admin panel
admin.site.register(WholesalerProfile)
admin.site.register(IoTNode)
admin.site.register(SensorLog)

# Advanced registration for better display in the admin panel
@admin.register(CropBatch)
class CropBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_id', 'crop', 'qty', 'status', 'days')
    search_fields = ('batch_id', 'crop', 'status')
    list_filter = ('status', 'crop')

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('crop', 'batch', 'qty', 'status', 'price', 'isAtRisk')
    search_fields = ('crop', 'batch', 'vendor')
    list_filter = ('status', 'isAtRisk')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('txn_id', 'buyerName', 'crop', 'total', 'status', 'time')
    search_fields = ('txn_id', 'buyerName', 'crop')
    list_filter = ('status', 'type')
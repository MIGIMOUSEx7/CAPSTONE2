from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WholesalerProfileViewSet, 
    IoTNodeViewSet, 
    CropBatchViewSet, 
    SensorLogViewSet,
    ListingViewSet,
    TransactionViewSet,
    request_password_reset,
    reset_password_confirm
)

router = DefaultRouter()


router.register(r'profiles', WholesalerProfileViewSet)
router.register(r'nodes', IoTNodeViewSet)
router.register(r'batches', CropBatchViewSet)
router.register(r'logs', SensorLogViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/request-reset/', request_password_reset, name='request_reset'),
        path('auth/reset-password/', reset_password_confirm, name='reset_confirm'),
]
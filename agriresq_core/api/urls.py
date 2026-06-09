from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WholesalerProfileViewSet, IoTNodeViewSet, CropBatchViewSet, SensorLogViewSet

router = DefaultRouter()
router.register(r'profiles', WholesalerProfileViewSet)
router.register(r'nodes', IoTNodeViewSet)
router.register(r'batches', CropBatchViewSet)
router.register(r'logs', SensorLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
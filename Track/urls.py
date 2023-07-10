from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet,DeviceViewSet,DeviceAllocationViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'devices', DeviceViewSet,basename="device")
router.register(r"deviceAllocation",DeviceAllocationViewSet,basename="deviceAllocation")
# router.register(r"devicelog",DeviceLogViewSet,basename="devicelog")

urlpatterns = [
    # Register the router URLs
    path('', include(router.urls)),
]

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, VentaViewSet, DetalleVentaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalles-venta', DetalleVentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

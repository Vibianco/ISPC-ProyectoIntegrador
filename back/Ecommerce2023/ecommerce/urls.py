from django.urls import path, include
from rest_framework import routers
from ecommerce.views import ProvinciaViewSet, Numeros_RifasViewSet, VentaViewSet, Medio_PagoViewSet
from ecommerce import views

router= routers.DefaultRouter()
router.register(r'provincia',views.ProvinciaViewSet)
router.register(r'numeros_rifas',views.Numeros_RifasViewSet)
router.register(r'venta',views.VentaViewSet)
router.register(r'medio_pago',Medio_PagoViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
]
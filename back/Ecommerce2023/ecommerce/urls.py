from django import urls
from django.urls import path, include, re_path
from rest_framework import routers
from ecommerce.views import ProvinciaViewSet, Numeros_RifasViewSet, VentaViewSet, Medio_PagoViewSet, UsuarioViewSet, FacturaViewSet, RifaViewSet
from ecommerce import views
from .views import *

router= routers.DefaultRouter()
router.register(r'usuario',views.UsuarioViewSet)
router.register(r'factura',views.FacturaViewSet)
router.register(r'rifa',views.RifaViewSet)
router.register(r'provincia',views.ProvinciaViewSet)
router.register(r'numeros_rifas',views.Numeros_RifasViewSet)
router.register(r'venta',views.VentaViewSet)
router.register(r'medio_pago',Medio_PagoViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
     
     path('auth/signup/', SigupView.as_view(), name='auth_signup'),
     path('auth/login/', LoginView.as_view(), name='auth_login'),
     path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    
     path('auth/list/', UserViewSet.as_view(), name='auth_user'),
     path('auth/update/<str:username>', UpdateUser.as_view(), name='actualizar_user'),
     path('auth/delete/<str:username>', DeleteUser.as_view(), name='eliminar_user'),
    
     path('rifa/add/', AddRifa.as_view(), name='agregar_rifa'),
     path('rifa/list/', ListRifa.as_view(), name='listar_rifa'),
     path('rifa/delete/<int:id_rifa>', DeleteRifa.as_view(), name='eliminar_rifa'),
     path('rifa/update/<int:id_rifa>', UpdateRifa.as_view(), name='actualizar_rifa'),
     
     path('retornarPagado/',
         retornarPagado.as_view(), name='retornarPagado'),
     path('actualizarstock/<int:pk>/<int:cantidad>', customjsonybajarstock.as_view(), name='customjsonybajarstock'),

]
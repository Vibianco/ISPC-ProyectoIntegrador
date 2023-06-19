from django.urls import path, include, re_path
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views

router= routers.DefaultRouter()
router.register(r'factura',FacturaViewSet)
router.register(r'rifa',RifaViewSet)
router.register(r'provincia',ProvinciaViewSet)
router.register(r'numeros_rifas',Numeros_RifasViewSet)
router.register(r'venta',VentaViewSet)
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
    path('rifa/filter/<str:nombre_sorteo>', ListRifaFilter.as_view(), name='filter_rifa'),
     
    path('auth/genToken', views.obtain_auth_token),

    path('carrito/list/', ListCarrito.as_view(), name='listar_carrito'),
    path('carrito/filter/<str:titulo_rifa>', ListCarritoFilter.as_view(), name='filter_rifa'),
    path('carrito/add/', AddCarrito.as_view(), name='añadir_carrito'),
    path('carrito/delete/<int:id_venta>', DeleteCarrito.as_view(), name='eliminar_carrito'),
    path('carrito/update/<str:titulo_rifa>', UpdateCarrito.as_view(), name='actualizar_carrito'),


    #  path('retornarPagado/',
    #      retornarPagado.as_view(), name='retornarPagado'),
    #  path('actualizarstock/<int:pk>/<int:cantidad>', customjsonybajarstock.as_view(), name='customjsonybajarstock'),

]
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProvinciaSerializer, Numeros_RifasSerializer, VentaSerializer, Medio_PagoSerializer, UsuarioSerializer, FacturaSerializer, RifaSerializer
from .models import Provincia, Numeros_Rifas, Venta, Medio_Pago, Usuario, Factura, Rifa

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class RifaViewSet(viewsets.ModelViewSet):
    queryset = Rifa.objects.all()
    serializer_class = RifaSerializer


class ProvinciaViewSet(viewsets.ModelViewSet):
 queryset=Provincia.objects.all()
 serializer_class= ProvinciaSerializer

class Numeros_RifasViewSet(viewsets.ModelViewSet):
 queryset=Numeros_Rifas.objects.all()
 serializer_class= Numeros_RifasSerializer

class VentaViewSet(viewsets.ModelViewSet):
 queryset=Venta.objects.all()
 serializer_class= VentaSerializer

class Medio_PagoViewSet(viewsets.ModelViewSet):
 queryset=Medio_Pago.objects.all()
 serializer_class= Medio_PagoSerializer
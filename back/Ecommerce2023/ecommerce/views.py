from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProvinciaSerializer, Numeros_RifasSerializer, VentaSerializer, Medio_PagoSerializer
from .models import Provincia, Numeros_Rifas, Venta, Medio_Pago

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
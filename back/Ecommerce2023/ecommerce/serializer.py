from rest_framework import serializers
from .models import Provincia, Numeros_Rifas, Venta, Medio_Pago, Usuario, Factura, Rifa

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'
    #fields = ('dni','nombre','apellido')

class FacturaSerializer(serializers.ModelSerializer):
  class Meta:
      model = Factura
      fields = '__all__'

class RifaSerializer(serializers.ModelSerializer):
  class Meta:
      model = Rifa
      fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
 class Meta:
  model= Provincia
  fields='__all__'

class Numeros_RifasSerializer(serializers.ModelSerializer):
 class Meta:
  model= Numeros_Rifas
  fields='__all__'

class VentaSerializer(serializers.ModelSerializer):
 class Meta:
  model= Venta
  fields='__all__'

class Medio_PagoSerializer(serializers.ModelSerializer):
 class Meta:
  model= Medio_Pago
  fields='__all__'
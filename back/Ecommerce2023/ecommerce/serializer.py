from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        required=True
    )
    password = serializers.CharField(
        min_length=8
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email', 
            'username', 
            'password',
            'nombre',
            'apellido',
            'DNI',
            'telefono',
            'provincia',
            'ciudad',
            )

    def validate_password(self, value):
        return make_password(value)
    
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
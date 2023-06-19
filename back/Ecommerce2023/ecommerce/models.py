from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import forms
       
class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True
    )
    DNI = models.CharField(max_length=50,null=False)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    telefono = models.CharField(max_length=15,null=False)
    provincia = models.CharField(max_length=15,null=False)
    ciudad = models.CharField(max_length=45,null=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

# Create your models here.

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    provincia = models.CharField(max_length=100,null=False,unique=True)
    class Meta:
        db_table="Provincia"
        verbose_name="Provincia del usuario"
        verbose_name_plural="Provincias"
    def __unicode__(self):
        return self.provincia
    def __str__(self):
        return self.provincia
  
class Medio_Pago(models.Model):
    id_medio_pago = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=45,null=False)
    class Meta:
        db_table="Medio_Pago"
        verbose_name="Medio de pago seleccionado o disponible"
        verbose_name_plural="Medios de pago"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True,null=False)
    #id_usuario = models.ForeignKey(Usuario,to_field ='id_usuario',null=True,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10,default=0,decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    fact_id_provincia = models.ForeignKey(Provincia,to_field ='id_provincia',null=True,on_delete=models.CASCADE)
    id_medio_pago = models.ForeignKey(Medio_Pago,to_field ='id_medio_pago',null=True,on_delete=models.CASCADE)
    class Meta:
        db_table="Factura"
        verbose_name="Factura de la compra"
        verbose_name_plural="Facturas"
    def __unicode__(self):
        return self.id_factura
    def __str__(self):
        return self.id_factura

class Rifa(models.Model):
    id_rifa = models.AutoField(primary_key=True)
    nombre_sorteo = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100,null=False)
    organizador = models.CharField(max_length=45,null=False)
    premio1 = models.CharField(max_length=100,null=False)
    premio2 = models.CharField(max_length=100)
    premio3 = models.CharField(max_length=100)
    cantidad_rifas = models.IntegerField(null=False)
    valor = models.DecimalField(max_digits=8,null=False,decimal_places=2)
#    fecha_sorteo = models.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    id_organizador = models.IntegerField()
    class Meta:
        db_table="Rifa"
        verbose_name="Rifas creadas"
        verbose_name_plural="Rifas"
    def __unicode__(self):
        return self.nombre_sorteo
    def __str__(self):
        return self.nombre_sorteo
    
class Numeros_Rifas(models.Model):
    id_numero = models.IntegerField(primary_key=True,default=1,validators=[MaxValueValidator(100),MinValueValidator(1)])
    id_rifa = models.ForeignKey(Rifa,to_field='id_rifa',null=True,on_delete=models.CASCADE)
    class Meta:
        db_table="Numeros_Rifas"
        verbose_name="Números de rifas"
        verbose_name_plural="Numeros_Rifas"
    def __unicode__(self):
        return self.id_numero
    def __str__(self):
        return self.id_numero

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_rifa = models.ForeignKey(Rifa,to_field='id_rifa',null=True,on_delete=models.CASCADE)
    cantidad = models.DecimalField(null=False,decimal_places=2,default=0,max_digits=10)
    id_factura = models.ForeignKey(Factura,to_field='id_factura',null=True,on_delete=models.CASCADE)
    descuento = models.DecimalField(null=False,decimal_places=2,default=0,max_digits=10)
    class Meta:
        db_table="Venta"
        verbose_name="Venta realizada"
        verbose_name_plural="Ventas"
    def __unicode__(self):
        return self.id_venta
    def __str__(self):
        return self.id_venta







    

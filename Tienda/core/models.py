from ast import Delete
from distutils.command.upload import upload
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from pyexpat import model
from ssl import PROTOCOL_TLS_CLIENT
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create Modelo para Categoria
 
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")
 
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID')
    idcategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoría')
    nombreProducto = models.CharField(max_length=80, verbose_name='Nombre')
    descripcion = models.TextField(default="INGRESAR DESCRIPCION", max_length=300)
    precio = models.IntegerField(default=0)
    porcDesctoSubscritor = models.IntegerField(default=0, verbose_name='Descuento subscriptor')
    porcDesctoOferta = models.IntegerField(default=0, verbose_name='Descuento por oferta')
    stock = models.IntegerField(default=0, verbose_name='Cantidad')
    Imagen = models.ImageField(upload_to="productos", null=True)


    def __str__(self):
        return self.nombreProducto
    
    


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    Password = models.CharField(max_length=50)
    EsSubscriptor = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
    
class Factura(models.Model):
    idFactura = models.IntegerField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    NroFactura = models.IntegerField()
    Fecha = models.DateField()
    EstadoFactura = models.CharField(max_length=1)

    def __str__(self):
        return self.NroFactura

class DetalleFactura(models.Model):
    idDetalleFac = models.IntegerField(primary_key=True)
    idFactura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    NroItem = models.IntegerField()
    precio = models.IntegerField()
    porcDesctoSubscriptor= models.IntegerField()
    porcDesctoOferta = models.IntegerField()
    PrecioFinal = models.IntegerField()

    def __str__(self):
        return self.idDetalleFac

class ProductosBodega(models.Model):
    idProdBodega = models.IntegerField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    idDetalleFac = models.ForeignKey(DetalleFactura, on_delete=models.PROTECT)

    def __str__(self):
        return self.idProdBodega



    


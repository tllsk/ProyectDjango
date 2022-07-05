from ast import Delete
from pyexpat import model
from ssl import PROTOCOL_TLS_CLIENT
from django.db import models

# Create your models here.
# Create Modelo para Categoria
 
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")
 
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    idcategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombreProducto = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=300)
    precio = models.IntegerField()
    porcDesctoSubscritor = models.IntegerField()
    porcDesctoOferta = models.IntegerField()
    UrlImagenProducto = models.CharField(max_length=300)
    Imagen = models.ImageField(upload_to="productos", null=True)


    def __str__(self):
        return self.nombreProducto

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    TipoUsuario = models.CharField(max_length=1)
    Rut = models.IntegerField() 
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=300)
    EsSubscriptor = models.BooleanField()
    Contrasena = models.CharField(max_length=50)
    UrlImagenUsuario = models.CharField(max_length=300)

    def __str__(self):
        return self.Nombres
    
    
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



    


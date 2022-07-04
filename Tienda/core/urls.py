from django.db import router
from django.urls import path, include 
from .views import index, ingresar, registrarse, nosotros, ropa, ficha, fichaRopa, cliente
from .views import carrito, detalle, fichaProducto, compras, datos, nosotrosCli
from .views import administrar, historial, mantenerB, mantenerP, mantenerU
from .views import agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)



urlpatterns = [
    path('', index, name="index"),
    path('ingresar/', ingresar, name="ingresar"),
    path('registrarse/', registrarse, name="registrarse"),
    path('nosotros/', nosotros, name="nosotros"),
    path('ropa/', ropa, name="ropa"),
    path('ficha/', ficha, name="ficha"),
    path('fichaRopa/', fichaRopa, name="fichaRopa"),
    path('cliente/', cliente, name="cliente"),
    path('carrito/', carrito, name="carrito"),
    path('detalle/', detalle, name="detalle"),
    path('fichaProducto/', fichaProducto, name="fichaProducto"),
    path('compras/', compras, name="compras"),
    path('datos/', datos, name="datos"),
    path('nosotrosCli/', nosotrosCli, name="nosotrosCli"),
    path('administrar/', administrar, name="administrar"),
    path('historial/', historial, name="historial"),
    path('mantenerB/', mantenerB, name="mantenerB"),
    path('mantenerP/', mantenerP, name="mantenerP"),
    path('mantenerU/', mantenerU, name="mantenerU"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name= "modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
]
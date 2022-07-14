from django.db import router
from django.urls import path, include


from .views import SuscritoViewset, agregar_procarrito, index, ingresar, limpiar_procarrito , registrarse, nosotros, ropa, ficha, fichaRopa, cliente, eliminar_procarrito,restar_procarrito,limpiar_procarrito
from .views import carrito, detalle, fichaProducto, compras, datos, nosotrosCli, mostrar_producto, agregar_procarrito3
from .views import administrar, historial, mantenerB, mantenerP, mantenerU, agregar_procarrito2, UsuarioViewset, UserViewset
from .views import agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, eliminar_producto2, ProductoViewset
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('usuario', UsuarioViewset)
router.register('user', UserViewset)
router.register('suscrito', SuscritoViewset)


urlpatterns = router.urls
urlpatterns += path('login',views.login),
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
    path('eliminar-producto2/<id>/',eliminar_producto2, name="eliminar_producto2"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('agregar/<int:producto_id>/',agregar_procarrito, name="Add"),
    path('agregar2/<int:producto_id>/',agregar_procarrito2, name="Add2"),
    path('agregar3/<int:producto_id>/',agregar_procarrito3, name="Add3"),
    path('eliminar/<int:producto_id>/',eliminar_procarrito, name="Del"),
    path('restar/<int:producto_id>/',restar_procarrito, name="Sub"),
    path('limpiar/',limpiar_procarrito, name="CLS"),
    path('mostrar-producto/<id>/', views.mostrar_producto, name= "mostrar_producto"),
    path('api/', include(router.urls)),
]






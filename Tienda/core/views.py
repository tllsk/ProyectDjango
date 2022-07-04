from itertools import product
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



# VISTA VISITA
def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/index.html',data)

def ingresar(request):
    return render(request, 'app/ingresar.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def ropa(request):
    return render(request, 'app/ropa.html')

def ficha(request):
    return render(request, 'app/ficha_producto.html')

def fichaRopa(request):
    return render(request, 'app/ficha_producto_ropa.html')

#VISTA CLIENTE
@login_required
def cliente(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/cliente/index.html',data)

@login_required
def carrito(request):
    return render(request, 'app/cliente/carrito.html')

@login_required
def detalle(request):
    return render(request, 'app/cliente/detalle_factura.html')

@login_required
def fichaProducto(request):
    return render(request, 'app/cliente/ficha_producto.html')

@login_required
def compras(request):
    return render(request, 'app/cliente/mis_compras.html')

@login_required
def datos(request):
    return render(request, 'app/cliente/mis_datos.html')


def nosotrosCli(request):
    return render(request, 'app/cliente/nosotros.html')

#VISTA ADMIN

@permission_required('app.change.producto')
def administrar(request):
    return render(request, 'app/cliente/administrar.html')
@permission_required('app.change.producto')
def historial(request):
    return render(request, 'app/cliente/historial_ventas.html')
@permission_required('app.change.producto')
def mantenerB(request):
    return render(request, 'app/cliente/mantenedor_bodega.html')
@permission_required('app.change.producto')
def mantenerP(request):
    return render(request, 'app/cliente/mantenedor_productos.html')
@permission_required('app.change.producto')
def mantenerU(request):
    return render(request, 'app/cliente/mantenedor_usuarios.html')

@permission_required('app.add.producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/admin/producto/agregar.html',data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request,'app/admin/producto/listar.html',data)

@permission_required('app.change.producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, idProducto=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'app/admin/producto/modificar.html',data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    producto.delete()
    return redirect(to="listar_productos")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to=cliente)
        data["form"] = formulario

    return render(request,'registration/registro.html',data)
    








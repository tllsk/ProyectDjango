from ast import FunctionDef
from itertools import product
from math import prod
from re import U
from urllib import response
from venv import create
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from requests import RequestException
from .models import Producto, User, Usuario, Account
from .forms import ProductoForm, CustomUserCreationForm, ProductoForm2, CustomUserCreationForm2, ProductoForm3
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, UsuarioSerializer, UserSerializer, SuscritoSerializer
from core.carrito import Carrito
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def login1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username='admin')
    except User.DoesNotExist:
        return Response("Usuario inválido")

    pwd_valid = check_password(password,user.password)

    if not pwd_valid:
        return Response("Contraseña invalida")

    token, _ = Token.objects.get_or_create(user=user)
    
    return Response(token.key)

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes=[IsAuthenticated]
    def get_queryset(self):
        productos = Producto.objects.all()

        nombreProducto = self.request.GET.get('nombreProducto')

        if nombreProducto:
            productos = productos.filter(nombreProducto__contains=nombreProducto)
        return productos

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SuscritoViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = SuscritoSerializer

class UserApi(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)





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

def agregar_procarrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def agregar_procarrito2(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("cliente")

def agregar_procarrito3(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")
    
    

def eliminar_procarrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_procarrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_procarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
    

@login_required
def carrito(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/cliente/carrito.html',data)

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







@permission_required('app.add.producto')
def agregar_producto(request):
    productos = Producto.objects.all()

    data = {
        'form': ProductoForm(),
        'productos': productos
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
        'form': ProductoForm2(),
        'productos': productos
    }
    if request.method == 'POST':
        formulario = ProductoForm2(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request,'app/admin/producto/listar.html',data)

@permission_required('app.change.producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, idProducto=id)

    data ={
        'form': ProductoForm3(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm3(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="agregar_producto")
        data["form"] = formulario

    return render(request, 'app/admin/producto/modificar.html',data)


def mostrar_producto(request, id):
    productos = get_object_or_404(Producto, idProducto=id)
    data = {
        'productos': productos
    }
    return render(request, 'app/cliente/mostrar.html',data)



@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    producto.delete()
    return redirect(to="agregar_producto")


@permission_required('app.delete_producto')
def eliminar_producto2(request, id):
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
            messages.success(request, 'Te has registrado correctamente')
            return redirect(to=cliente)
        data["form"] = formulario

    return render(request,'registration/registro.html',data)

def mantenerU(request):
    user = User.objects.all()
    data={
        'form': CustomUserCreationForm(),
        'user': user
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm2(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
            
    if request.method == 'POST':
        formulario = CustomUserCreationForm2(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to=cliente)
        data["form"] = formulario

    return render(request,'app/cliente/mantenedor_usuarios.html',data)



from dataclasses import field
from tabnanny import verbose
from .models import Producto, Usuario, Account
from rest_framework import serializers
from django.contrib.auth.models import User



class ProductoSerializer(serializers.ModelSerializer):

    nombreProducto = serializers.CharField(required = True, max_length=80)

    def validate_nombreProducto(self, value):
            existe = Producto.objects.filter(nombreProducto__iexact=value).exists()

            if existe:
                raise serializers.ValidationError("Este Producto ya existe")

            return value

    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

class SuscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, Ingrese uno nuevo")
        else:
            return data

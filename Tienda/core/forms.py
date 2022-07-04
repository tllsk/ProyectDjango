from msilib.schema import Class
from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductoForm(forms.ModelForm):

    nombreProducto = forms.CharField(min_length=3, max_length=80)

    class Meta:
        model = Producto
        fields = '__all__'

    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username', "first_name", "last_name", "email", "password1", "password2"]
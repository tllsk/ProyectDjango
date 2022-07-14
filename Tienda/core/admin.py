from django.contrib import admin
from core.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from.models import Categoria, Producto, Usuario, Factura, DetalleFactura, ProductosBodega
# Register your models here.

class AccountInLine(admin.StackedInline):
    model = Account
    ccan_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombreProducto", "precio", "descripcion"]
    list_editable = ["precio"]  
    search_fields = ["nombreProducto"]
    list_filter = ["idcategoria"]


class UsuarioAdmin(admin.ModelAdmin):
    list_filter = ["esSubscriptor"]



admin.site.register(Categoria)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(ProductosBodega)
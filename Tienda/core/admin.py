from django.contrib import admin
from.models import Categoria, Producto, Usuario, Factura, DetalleFactura, ProductosBodega
# Register your models here.

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
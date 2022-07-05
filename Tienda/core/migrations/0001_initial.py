# Generated by Django 4.0.4 on 2022-06-25 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=80, verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('idDetalleFac', models.IntegerField(primary_key=True, serialize=False)),
                ('NroItem', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('porcDesctoSubscriptor', models.IntegerField()),
                ('porcDesctoOferta', models.IntegerField()),
                ('PrecioFinal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=80)),
                ('descripcion', models.TextField(max_length=300)),
                ('precio', models.IntegerField()),
                ('porcDesctoSubscritor', models.IntegerField()),
                ('porcDesctoOferta', models.IntegerField()),
                ('UrlImagenProducto', models.CharField(max_length=300)),
                ('idcategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('TipoUsuario', models.CharField(max_length=1)),
                ('Rut', models.IntegerField()),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('Direccion', models.IntegerField()),
                ('EsSubscriptor', models.CharField(max_length=1)),
                ('Contrasena', models.CharField(max_length=50)),
                ('UrlImagenUsuario', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosBodega',
            fields=[
                ('idProdBodega', models.IntegerField(primary_key=True, serialize=False)),
                ('idDetalleFac', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.detallefactura')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('idFactura', models.IntegerField(primary_key=True, serialize=False)),
                ('NroFactura', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('EstadoFactura', models.CharField(max_length=1)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='idFactura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.factura'),
        ),
    ]

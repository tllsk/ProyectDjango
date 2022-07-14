# Generated by Django 3.1.2 on 2022-07-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_imagen_alter_usuario_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='UrlImagenProducto',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='EsSubscriptor',
            field=models.BooleanField(),
        ),
    ]
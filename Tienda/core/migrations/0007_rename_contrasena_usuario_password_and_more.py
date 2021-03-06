# Generated by Django 4.0.6 on 2022-07-14 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220707_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Contrasena',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Direccion',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Apellidos',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombres',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Rut',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='TipoUsuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='UrlImagenUsuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='EsSubscriptor',
            field=models.BooleanField(default=False),
        ),
    ]

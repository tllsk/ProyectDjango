# Generated by Django 3.1.2 on 2022-07-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220706_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
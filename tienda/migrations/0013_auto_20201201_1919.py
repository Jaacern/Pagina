# Generated by Django 3.1.3 on 2020-12-01 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_auto_20201129_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='procesada',
            new_name='venta_procesada',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_servicioportalrrhh_cliente_serviciocontable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
    ]
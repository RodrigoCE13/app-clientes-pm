# Generated by Django 4.2.2 on 2023-06-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ServicioPortalRRHH',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='servicioContable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='servicioRemuneraciones',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='banco',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='claveCertificadoDigital',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clavePrevired',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='claveSII',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='claveSIIRepresentante',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='emailContacto1',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='emailContacto2',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombreContacto1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombreContacto2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombreDeFantasia',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numeroCuenta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='otroServicio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='regimenTributario',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='representanteLegal',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rutEmpresa',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rutRepresentanteLegal',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefonoContacto2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipoCuenta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuarioPrevired',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='vencimientoCertificadoDigital',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
    ]

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombreDeFantasia=models.CharField(max_length=100)
    rutEmpresa=models.CharField(max_length=20)
    razonSocial=models.CharField(max_length=100)
    fechaIngresoCliente=models.DateField(max_length=10)
    claveSII=models.CharField(max_length=100)
    nombreContacto1=models.CharField(max_length=100)
    telefonoContacto1=models.CharField(max_length=20)
    emailContacto1=models.EmailField(max_length=100)
    nombreContacto2=models.CharField(max_length=100)
    telefonoContacto2=models.CharField(max_length=20)
    emailContacto2=models.EmailField(max_length=100)
    representanteLegal=models.CharField(max_length=100)
    rutRepresentanteLegal=models.CharField(max_length=20)
    banco=models.CharField(max_length=100)
    tipoCuenta=models.CharField(max_length=100)
    numeroCuenta=models.CharField(max_length=50)
    claveSIIRepresentante=models.CharField(max_length=50)
    inicioActividades=models.DateField(max_length=10)
    regimenTributario=models.CharField(max_length=100)
    claveCertificadoDigital=models.CharField(max_length=100)
    vencimientoCertificadoDigital=models.DateField(max_length=10)
    usuarioPrevired=models.CharField(max_length=100)
    clavePrevired=models.CharField(max_length=100)
    otroServicio=models.CharField(max_length=100)

    estado=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreDeFantasia
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombreDeFantasia=models.CharField(max_length=60,null=True,blank=True)
    rutEmpresa=models.CharField(max_length=30)
    razonSocial=models.CharField(max_length=100)
    fechaIngresoCliente=models.DateField(max_length=10)
    claveSII=models.CharField(max_length=30)
    nombreContacto1=models.CharField(max_length=50)
    telefonoContacto1=models.CharField(max_length=20)
    emailContacto1=models.EmailField(max_length=60)
    nombreContacto2=models.CharField(max_length=50,null=True,blank=True)
    telefonoContacto2=models.CharField(max_length=20,null=True,blank=True)
    emailContacto2=models.EmailField(max_length=60,null=True,blank=True)
    representanteLegal=models.CharField(max_length=50)
    rutRepresentanteLegal=models.CharField(max_length=30)
    banco=models.CharField(max_length=50,null=True,blank=True)
    tipoCuenta=models.CharField(max_length=50,null=True,blank=True)
    numeroCuenta=models.CharField(max_length=50,null=True,blank=True)
    claveSIIRepresentante=models.CharField(max_length=30,null=True,blank=True)
    inicioActividades=models.DateField(max_length=10)
    regimenTributario=models.CharField(max_length=60)
    claveCertificadoDigital=models.CharField(max_length=30,null=True,blank=True)
    vencimientoCertificadoDigital=models.DateField(max_length=10,null=True,blank=True)
    usuarioPrevired=models.CharField(max_length=60,null=True,blank=True)
    clavePrevired=models.CharField(max_length=30,null=True,blank=True)
    servicioContable=models.BooleanField(default=False,null=True,blank=True)
    servicioRemuneraciones=models.IntegerField(null=True,blank=True)
    ServicioPortalRRHH=models.BooleanField(default=False,null=True,blank=True)
    otroServicio=models.CharField(max_length=100,null=True,blank=True)

    estado=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.razonSocial+' - '+self.rutEmpresa
    
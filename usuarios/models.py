from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nombreDeUsuario=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50)
    rol_usuario=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,null=True,blank=True)
    estado=models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
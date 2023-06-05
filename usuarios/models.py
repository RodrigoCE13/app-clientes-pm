from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    rol_user=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    estado=models.BooleanField(default=True)

    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
from django.db import models
from django.core.exceptions import ValidationError

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    numero_apartamento = models.CharField(max_length=6)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(unique=True)

class Vehiculo(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')  # Cambia aquí si es necesario
    matricula = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.correo}"
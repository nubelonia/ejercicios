from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "evento"

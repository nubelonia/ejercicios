from django.db import models

'''
- Crea un modelo llamado Hotel con los atributos: nombre, categoría,
dirección, teléfono, correo electrónico, año de creación y número de
habitaciones.
- El método __str__ debe retornar nombre del hotel, categoría, año de
creación y número de habitaciones.

'''

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    ano_creacion = models.PositiveIntegerField()
    numero_habitaciones = models.PositiveIntegerField()

    def __str__(self):
        return f"Hotel: {self.nombre} - Categoría: {self.categoria} - Año: {self.ano_creacion}, Habitaciones: {self.numero_habitaciones}"


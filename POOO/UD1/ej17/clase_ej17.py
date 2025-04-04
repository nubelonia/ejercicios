'''
Debemos diseñar una aplicación Python que permita gestionar una lista de vehículos.
a. Cada vehículo tiene como atributos: matrícula, marca, modelo, color, año, kilómetros, 
potencia y una lista de fechas en las que ha sido reparado.
b. Dos vehículos se consideran iguales si tienen la misma matrícula.
c. El constructor no recibe la lista de fechas como parámetro, sino que existe un método
llamado agregar_reparación que añade una fecha a la lista.

Los métodos asociados a la lista de vehículos son:

    - Añadir vehículo. No pueden existir varios vehículos con idéntica matrícula.
    - Retornar el número de reparaciones de un vehículo, a partir de su matrícula.
    - Eliminar un vehículo de la lista conociendo su matrícula.
    - Ordenar la lista de vehículos por año de compra.
    - Añadir reparación a un vehículo. Recibe matrícula y fecha de reparación.
    - Mostrar todos los vehículos.
    
'''

class Vehiculo:
    def __init__(self, matricula, marca, modelo, color, anio, kilometros, potencia):

        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.kilometros = kilometros
        self.potencia = potencia
        # Este atributo es sin parámetro. En este caso mediante el método agregar_reparacion 
        # añade la fecha a la lista vacía 
        self.fechas_reparaciones = []
    
    # No pueden existir varios vehículos con idéntica matrícula.
    def __eq__(self, otro_vehiculo):
        return self.matricula == otro_vehiculo.matricula
        
    def __str__(self):
        return f"Matricula: {self.matricula} - Marca: {self.marca} - modelo: {self.modelo} - color: {self.color} - año: {self.anio} - Kms: {self.kilometros} - potencia: {self.potencia} CV - Reparaciones: {self.fechas_reparaciones} "
    
    
    # Método para agregar fechas de reparaciones
    def agregarReparacion(self, fecha):
        self.fechas_reparaciones.append(fecha)    


class ListaVehiculos:

        lista_vehiculos = [
Vehiculo("ABC123", "Toyota", "Corolla", "Rojo", 2019, 20000, 150),
Vehiculo("DEF456", "Nissan", "Sentra", "Azul", 2018, 18000, 140),
Vehiculo("GHI789", "Chevrolet", "Spark", "Blanco", 2017, 160400, 130),
Vehiculo("JKL012", "Mazda", "3", "Negro", 2016, 15000, 120),
Vehiculo("KKL122", "Volkswagen", "Golf", "Blanco", 2020, 230400, 120),
Vehiculo("MMG122", "Nissan", "Micra", "Azul", 2020, 123000, 86),
Vehiculo("ZZE123", "Seat", "Ibiza", "Blanco", 2010, 67000, 120),
]
               
        

        # Método para añadir un vehículo si no tiene matrícula repetida
        @classmethod
        def agregar_vehiculo(cls, vehiculo):
            if vehiculo.matricula in [v.matricula for v in cls.lista_vehiculos]:
                print(f"No se puede agregar. Ya existe un vehículo con la matrícula {vehiculo.matricula}.")
            else:
                cls.lista_vehiculos.append(vehiculo)
                print(f"Vehículo con matrícula {vehiculo.matricula} agregado exitosamente.")

        # Método para mostrar todos los vehículos en la lista
        @classmethod
        def mostrar_vehiculos(cls):
            for vehiculo in cls.lista_vehiculos:
                print(vehiculo)
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
    
    # No pueden existir dos vehículos con idéntica matrícula.
    def __eq__(self, otro_vehiculo):
        return self.matricula == otro_vehiculo.matricula
        
    def __str__(self):
        return f"Matricula: {self.matricula} - Marca: {self.marca} - modelo: {self.modelo} - color: {self.color} - año: {self.anio} - Kms: {self.kilometros} - potencia: {self.potencia} CV - Reparaciones: {self.fechas_reparaciones} "
    
    
    # Método para agregar fechas de reparaciones
    def agregar_reparacion(self, fecha):
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
               
        

        # Buscar vehículo por matrícula (ignora mayúsculas/minúsculas). Con esto se consigue comprobar
        # si ya existe ese vehículo en la lista. Si no es asi, se puede añadir el vehículo.
        @classmethod
        def buscar_por_matricula(cls, matricula):
            for vehiculo in cls.lista_vehiculos:
                if vehiculo.matricula.lower() == matricula.lower():
                    return vehiculo
            return None
        


        # Añadir vehículo si no tiene matrícula repetida
        @classmethod
        def agregar_vehiculo(cls, vehiculo):
            if cls.buscar_por_matricula(vehiculo.matricula):
                print(f"No se puede agregar. Ya existe un vehículo con la matrícula {vehiculo.matricula}.")
            else:
                cls.lista_vehiculos.append(vehiculo)
                print(f"Vehículo con matrícula {vehiculo.matricula} agregado exitosamente.")


        

        

        
        # Retornar el número de reparaciones de un vehículo, a partir de su matrícula
        @classmethod
        def numero_reparaciones_vehiculo(cls, matricula):
            vehiculo = cls.buscar_por_matricula(matricula)
            if vehiculo:
                return len(vehiculo.fechas_reparaciones)
            else:
                return -1  # Vehículo no encontrado   


        

        # Eliminar un vehículo de la lista conociendo su matrícula.
        @classmethod
        def eliminar_vehiculo(cls, matricula):
            vehiculo = cls.buscar_por_matricula(matricula)  # Usamos buscar_por_matricula
            if vehiculo:  # Si el vehículo existe
                cls.lista_vehiculos.remove(vehiculo)  # Eliminamos directamente el objeto de la lista
                return True
            return False  # Si no existe, retornamos False


        '''
        Esto lo propone el curso:
        # Eliminar un vehículo de la lista conociendo su matrícula.
        @classmethod
        def eliminar_vehiculo(cls, matricula):
            for i in range(len(cls.lista_vehiculos)):    # 0 ---- 5
                if cls.lista_vehiculos[i].matricula == matricula:
                    del cls.lista_vehiculos[i]
                return True
            return False              
        '''





        # Ordenar la lista de vehículos por año de compra.
        @classmethod
        def ordenar_por_anio(cls, rever):
            cls.lista_vehiculos.sort(key= lambda v: v.anio, reverse=rever)

        
        '''
        Otra alternativa:

        # Ordenar la lista de vehículos por año de compra.
        @classmethod
        def ordenar_por_anio(cls, ascendente=True):
            cls.lista_vehiculos.sort(key=lambda vehiculo: vehiculo.anio, reverse=not ascendente)

        '''


        
        
        
        # Añadir reparación a un vehículo. Recibe matrícula y fecha de reparación.
        @classmethod
        def agregar_reparacion_por_matricula(cls, matricula, fecha):
            vehiculo = cls.buscar_por_matricula(matricula)
            if vehiculo:
                vehiculo.agregar_reparacion(fecha)
                print(f"Reparación con fecha: {fecha} añadida al vehículo con matrícula: {matricula}.")
            else:
                print(f"No se encontró ningún vehículo con matrícula {matricula}.")

        


        # Mostrar todos los vehículos.
        @classmethod
        def mostrar_todos(cls):
            print(*cls.lista_vehiculos, sep="\n")

        '''
        Otra alternativa:

        # Mostrar todos los vehículos en la lista
        @classmethod
        def mostrar_vehiculos(cls):
            for vehiculo in cls.lista_vehiculos:
                print(vehiculo)
        '''
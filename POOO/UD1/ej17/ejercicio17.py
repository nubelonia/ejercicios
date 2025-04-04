'''
c. El constructor no recibe la lista de fechas como parámetro, sino que existe un método
llamado agregar_reparación que añade una fecha a la lista.
Los métodos asociados a la lista de vehículos son:
- Añadir vehículo. No pueden existir varios vehículos con idéntica matrícula.

'''

from clase_ej17 import *
from datetime import date

# Añadimos vehiculo con el método agregar_vehiculo()
auto1 = Vehiculo("XYZ999", "Ford", "Focus", "Gris", 2021, 5000, 160)
auto2 = Vehiculo("XYZ999", "Ford", "Focus", "Gris", 2021, 5000, 160)

ListaVehiculos.agregar_vehiculo(auto1)
ListaVehiculos.agregar_vehiculo(auto2)  # Aquí sí debería saltar el mensaje de duplicado

ListaVehiculos.mostrar_vehiculos()


# Añadir reparacion

auto1 = ListaVehiculos.agregarReparacion('XYZ999', date(2025, 3, 3))
auto1 = ListaVehiculos.agregarReparacion('XYZ999', date(2025, 4, 2))



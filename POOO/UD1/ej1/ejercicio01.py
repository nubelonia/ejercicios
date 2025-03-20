'''
1. Diseñar una clase llamada “Vehículo” con los atributos marca, modelo, año y precio.
Crear dos objetos pertenecientes a esa clase e imprimir en pantalla la marca, el
modelo y el precio de cada vehículo (mediante __str__).

'''

#Importamos desde el modulo clases_ej1 la clase Vehiculo
from clases_ej1 import Vehiculo

# Instanciamos (crear objeto) varios vehiculos. Marca y modelo es de tipo string
# Año y precio es de tipo númerico (sin comillas)

v1 = Vehiculo("Ford","Fiesta", 1993, 4000)
v2 = Vehiculo("Renault","Clio", 1994, 3500)
v3 = Vehiculo("Opel","Mokka", 1996, 6000)

print(v1)
print(v2)
print(v3)


'''
Salida:
Marca: Ford - modelo: Fiesta - año: 1993 - precio: 4000
Marca: Renault - modelo: Clio - año: 1994 - precio: 3500
Marca: Opel - modelo: Mokka - año: 1996 - precio: 6000

'''


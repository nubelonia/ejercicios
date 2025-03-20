'''
2. En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y
añadiremos un método llamado “nombre_completo” que retorne en una cadena los
atributos marca y modelo concatenados y separados por un guión (Seat-Ibiza).
Crear dos objetos y probar el método.

'''
from clases_ej2 import Vehiculo

v1 = Vehiculo("Ford","Fiesta", 1993, 4000)
v2 = Vehiculo("Renault","Clio", 1994, 3500)
v3 = Vehiculo("Opel","Mokka", 1996, 6000)

print(v1.nombre_completo())
print(v2.nombre_completo())
print(v3.nombre_completo())

'''
Salida:
Ford - Fiesta
Renault - Clio
Opel - Mokka

'''

'''
Diseñar la clase “Empleado” con los atributos identificador, nombre, 
departamento, salario. Tener en cuenta que el salario será privado. 
Define un método para obtenerlo y otro para modificarlo. 
Programa el método eq(), de forma que indique si dos empleados 
son iguales o no en función de su salario.
Crear varios empleados, mostrar sus datos y comparar si son iguales o no.

'''
from clase_ej11 import Empleado

p1 = Empleado(1, "Armando", "Contabilidad", 2000)
p2 = Empleado(2, "Domingo", "RRHH", 2000)
p3 = Empleado(3, "Perico", "Informática", 4000)

# Mostrar datos de los empleados
print(p1.mostrar_datos())
print(p2.mostrar_datos())
print(p3.mostrar_datos())

# Comparar empleados
print(f"¿Armando y Domingo tienen el mismo salario? {p1 == p2}")
print(f"¿Armando y Perico tienen el mismo salario? {p1 == p3}")

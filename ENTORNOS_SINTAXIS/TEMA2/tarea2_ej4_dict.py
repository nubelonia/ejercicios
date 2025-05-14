estudiante = {"nombre": "Juan", "edad": 20,"carrera": "Informática", "notas": [8.5, 9.0, 7.5,
10] }
# 1. Añade una nueva clave instituto con el valor "Suarez de Figueroa".
estudiante.update({"instituo": "Suarez de Figueroa"})

# 2. Modifica la edad del estudiante a 21 años.
estudiante.update({"edad": "21"})
print(estudiante)

# 3. Imprime la clave “beca”, si no existe, que imprima la cadena “Error”.
print(estudiante["beca"])

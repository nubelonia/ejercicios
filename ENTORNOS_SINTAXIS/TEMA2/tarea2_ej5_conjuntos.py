conjunto1 = {1, 2, 3, 4, 5} 
conjunto2 = {4, 5, 6, 7, 8}
# 1. Calcula la unión de los dos conjuntos y guárdala en una nueva variable.
union = conjunto1 | conjunto2
# 2. Calcula la intersección de los conjuntos y guárdala en otra variable.
interseccion = conjunto1 & conjunto2
# 3. Calcula la diferencia de conjunto1 menos conjunto2.
diferencia = conjunto1 - conjunto2
# 4. Añade el número 9 a conjunto1 y elimina el número 2.
conjunto1.add(9)
conjunto1.remove(2)
# 5. Imprime los resultados de las operaciones.
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Conjunto1 modificado:", conjunto1)




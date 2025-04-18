from clases_ejercicio1_ud1 import Producto

# - Instancia dos objetos.

p1 = Producto(1, "Pepsi", "Refrescos", 1.50, 30, 20)
p2 = Producto(2, "Pascual", "Leche", 1.20, 20, 40)


# - Imprime ambos objetos.

print(p1)
print(p2)

# - Actualiza las unidades del primero.

p1.actualizar_stock(40)

# - Imprime el primer objeto.

print(p1)



# - Comprueba si el segundo está en mínimos.

print(p2.esta_en_minimos())




# - Comprueba si son iguales.

print (p1 == p2)
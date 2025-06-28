import numpy as np

# Array con las notas de matemáticas 
nota_mat = np.array([6.3, 9.1, 7.2 , 4.8, 7.2, 4.4, 5.5, 4.2, 6.9, 3.3, 4.5, 5.6, 5.4, 6.8, 5.1])

# Creamos un array del mismo tamaño y tipo que nota_mat, con todos los valores a 1
nuevo = np.ones_like(nota_mat)
print("Nuevo (a 1):", nuevo)

# Sumamos ambos arrays de forma vectorizada
suma = nota_mat + nuevo
print("Suma:", suma)

# Multiplicamos cada valor del array suma por 3
multiplica = suma * 3
print("Multiplicación:", multiplica)

# Calculamos la raíz cuadrada de cada elemento del array multiplicado
raiz = np.sqrt(multiplica)
print("Raíz cuadrada:", raiz)

# Redondeamos cada elemento de la raíz al entero más cercano
resultado = np.round(raiz)
print("Resultado redondeado:", resultado)

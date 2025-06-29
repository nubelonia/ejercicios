'''
Ejercicio 1
Crea un array a partir de una lista de números con decimales (los que tu consideres, 4 o 5 números). Imprime sus valores uno a uno mediante
un bucle while y los atributos del array (dimensiones, tamaño, tipo de dato, shape).
'''

import numpy as np
# Lista para crear el array a partir de ella
lista = [4.5, 7.36, 7., 0.56]
# Creamos el array mediante la estructura lista
mi_array = np.array(lista)
indice=0
tam = mi_array.size # Guardamos en tam el tamaño del array

print("RESULTADOS EJERCICIO 1")
print("Elementos del array:")
# Recorremos el array con un while desde indice=0 hasta tam-1
while indice < tam:
    print(mi_array[indice]) # Imprimimos el valor del array en su posición [indice]
    indice+=1

print("Tamaño:", tam)
print("Tipo de dato:", mi_array.dtype)
print("Shape:", mi_array.shape)
print("Dimensiones:", mi_array.ndim)



'''
Ejercicio 2
Crear una función “inicializar_array” que reciba por parámetro un array de 1 dimensión de tipos enteros y devuelva el array inicializado/
modificado con valores introducidos por teclado (solamente enteros). Utilizar un while para recorrer el array.
'''

def iniciar_array(array):
    tam = array.size
    indice = 0
    # Recorremos el array desde indice=0 hasta (array.size - 1)
    while indice < tam:
        item = int(input("Introduce un entero:"))
        # El item introducido por teclado lo guardamos en array[indice]
        array[indice] = item
        indice+=1
    return array

print("RESULTADOS EJERCICIO 2")

# Creamos un array cualquiera
mi_array = np.arange(6)
print(mi_array)
print(mi_array.dtype)
# Invoco la función iniciar_array para modificar dentro su contenido
array_mod = iniciar_array(mi_array)
# Como puedes ver, tanto el array original como el array retornado de la función son el mismo
# Esto es porque los parámetros de tipo estructuras se pasan como puntero a su dirección de memoria
print(mi_array)
print(array_mod)


'''
Ejercicio 3
Crear las funciones “media”, “máximo”, “mínimo” que reciba un array de valores numéricos y devuelva la media aritmética, el valor máximo y el
valor mínimo respectivamente. Realizar el cálculo manualmente recorriendo el array con un while.
'''

def media(array):
    tam = array.size
    indice = 0
    suma = 0
    while indice < tam:
        suma += array[indice]
        indice+=1
    return suma/tam

def maximo(array):
    tam = array.size
    indice = 1
    maximo = array[0]
    while indice < tam:
        if array[indice] > maximo:
            maximo = array[indice]
        indice+=1
    return maximo


def minimo(array):
    tam = array.size
    indice = 1
    minimo = array[0]
    while indice < tam:
        if array[indice] < minimo:
            minimo = array[indice]
        indice+=1
    return minimo

print("RESULTADOS EJERCICIO 3")

mi_array = np.array([1, -5, 8, 25, -7, 4, 0, 14])
print(mi_array)
print("La media es:", media(mi_array))
print("Valor máximo:", maximo(mi_array))
print("Valor mínimo:", minimo(mi_array))
print(f"Media={mi_array.mean()}. Mínimo={mi_array.min()}. Máximo={mi_array.max()}")


'''
Crear la función “encontrar” (usando while) que reciba dos parámetros: un array numérico y un valor. La función debe buscar en el array si el
“valor” se encuentra en él. La función debe devolver:
• Si valor se encuentra en el array, devolver el índice (primera aparición)
• Si el valor no se encuentra en el array, devolver -1.
'''

def encontrar(array, valor):
    tam = array.size
    indice = 0
    # Para encontrar un valor recorremos el array desde índice=0 hasta size-1
    while indice < tam:
        # Comprobamos cada elemento por el valor a encontrar
        if array[indice] == valor:
            # Si coincide, realizamos un return del índice y así acaba la función
            return indice
        indice+=1
    # Si acaba el while sin encontrar el valor significa que no existe, return -1
    return -1

print("RESULTADOS EJERCICIO 4")
mi_array = np.array([1, -5, 8, 25, -7, 8, 0, 14])
print(encontrar(mi_array, 15))

'''
Ejercicio 5
Crear una función “desviación estándar” que reciba por parámetro un array y devuelva la desviación estándar. Calcular paso a paso el
resultado utilizando un while para recorrer el array. También se debe usar la función “media” del ejercicio 2. Para calcular la raíz cuadrada
podemos usar la función de numpy.sqrt(n). Operador potencia es **
'''

def desviacion_estandar(array):
    # Calculamos la media mediante la función anteriormente realizada
    media_array = media(array)

    tam = array.size
    indice = 0
    sumatorio = 0
    # Calculamos sumatorio de (array[i] - media_array)^2 mediante un while
    while indice < tam:
        sumatorio += (array[indice] - media_array) ** 2
        indice+=1

    # Dividimos el sumatorio entre N y calculamos la raiz cuadrada. Devolviendo el resultado
    return np.sqrt(sumatorio / tam)

print("RESULTADOS EJERCICIO 5")
# Creamos un array cualquiera e invocamos a la función
mi_array = np.array([1, -5, 8, 25, -7, 8, 0, 14])
print("Desviación estándar cálculo manual:", desviacion_estandar(mi_array))
print("Desviación estándar función NumPy :", np.std(mi_array))
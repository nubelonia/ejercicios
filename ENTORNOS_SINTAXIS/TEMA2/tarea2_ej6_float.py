# 1. Solicita por consola un número flotante (real).
numero_flotante = float(input("Por favor, teclea un número decimal: "))

# 2. Convierte el número a entero.
numero_entero = int(numero_flotante)
print("La parte entera es: ", numero_entero)

# 3. Calcula el cuadrado del número y verifica si es mayor que 1000.
cuadrado = numero_entero ** 2
if cuadrado > 1000:
    print("El cuadrado es grande")
else:
    print("El cuadrado es pequeño")

# 4. Calcula si el número entero es par e imprímelo por pantalla.
if numero_entero % 2 == 0: # Si el resto es igual a 0, es par
    print(f"El número {numero_entero} es par.")
else:
    print(f"El número {numero_entero} es impar.")
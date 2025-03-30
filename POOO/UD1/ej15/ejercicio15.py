'''
Diseña una aplicación Python que gestione una lista de ciudades. De cada ciudad se guarda nombre, población, país y continente. Se considera que dos ciudades son iguales si tienen el mismo nombre y país.
La gestión de ciudades incluirá la creación de una clase que contenga métodos para:

    Mostrar las ciudades de un continente dado.
    Mostrar las ciudades con una población mayor que un número dado.
    Retornar el número de ciudades de un país dado.
    Retornar el número de ciudades que contienen una cadena en su nombre.
    Retornar la media de la población de las ciudades de un país.
    Retornar una lista con las ciudades de un país.
    Retornar una lista con las ciudades de un continente.
    Retornar la suma de los habitantes de todas las ciudades.
    Añadir ciudad. Este método recibe un objeto ciudad como parámetro e
    intenta añadir esa ciudad a la lista. Si la ciudad está en la lista no podrá
    añadirla y retornará False. En caso de añadirla el retorno será True. Para
    comprobar si un valor está en una lista se puede utilizar:
        if valor in lista
        if valor not in lista
        Aquí tienes una lista de ciudades que te pueden interesar.

'''

from clase_ej15 import *


###########################
'''
Mostrar las ciudades de un continente dado.
'''

# Para crear un input, o que nos pida que continente queremos
continente_buscado = input("Introduce continente: ")

# Esta variable "ciudades" será para que tengamos acceso al listado de ciudades 
# creada en la clase mediante el método de clase mostrar_ciudades_continente
ciudades = ListaCiudades.mostrar_ciudades_continente(continente_buscado)

if ciudades:
    print(f"\nCiudades en {continente_buscado}:")
    for ciudades_continente in ciudades:
        print(ciudades_continente)
else:
    print(f"No se encontraron ciudades en el continente {continente_buscado}")


###########################

'''
Mostrar las ciudades con una población mayor que un número dado.
'''

cantidad_poblacion = input("Introduce población: ")

# Ahora hay que convertir el input a entero
try:
    cantidad_poblacion = int(cantidad_poblacion)
except ValueError:
    print("X Error: Debes ingresar un número entero válido")
    exit()

ciudades_por_poblacion = ListaCiudades.mostrar_por_población(cantidad_poblacion)

if ciudades_por_poblacion:
    print(f"\nCiudades con mayor población de: {cantidad_poblacion} habitantes")
    for ciudades_habitantes in ciudades_por_poblacion:
        print(ciudades_habitantes)
else:
    print(f"No hay ciudades con más de {cantidad_poblacion} habitantes.")



###########################
'''
Retornar el número de ciudades de un país dado.
'''
pais_introducido = input("Introduce nombre del pais: ")
lista_ciudades_pais = ListaCiudades.mostrar_ciudades_pais(pais_introducido)

if ciudades:
    print(f"\nCiudades en {pais_introducido}:")
    for ciudades_pais in lista_ciudades_pais:
        print(ciudades_pais)
else:
    print(f"No se encontraron ciudades en ese pais {pais_introducido}")


###########################

'''
Retornar el número de ciudades que contienen una cadena en su nombre.
'''

cadena_introducida = input("Introduce cadena: ")
ciudades_con_cadena = ListaCiudades.contar_ciudades_cadena(cadena_introducida)

if ciudades_con_cadena > 0:
    print(f"\nCantidad de ciudades que contienen '{cadena_introducida}': {ciudades_con_cadena}")
else:
    print(f"No se encontraron ciudades que contengan '{cadena_introducida}'")


###########################

'''
Retornar la media de la población de las ciudades de un país.
'''

pais_introducido_media = input("Introduce el nombre de un país para calcular la media poblacional: ")

media = ListaCiudades.media_poblacion_por_pais(pais_introducido_media)

if media is not None:
    print(f"\nLa población media de las ciudades en {pais_introducido_media} es: {media:.2f} habitantes.")
else:
    print(f"\nNo se encontraron ciudades en {pais_introducido_media}.")



###########################

'''
Retornar una lista con las ciudades de un país.

'''

pais_introducido_lista_ciudades = input("Listar ciudades por páis. Introduce nombre del pais: ")
lista_ciudades_pais = ListaCiudades.listaCiudades_pais(pais_introducido_lista_ciudades)


if lista_ciudades_pais: #Verifica si la lista no está vacia 
    print(f"\nCiudades en {pais_introducido_lista_ciudades}:")
    for ciudad in lista_ciudades_pais:
        print(ciudad)
else:
    print(f"No se encontraron ciudades en  {pais_introducido_lista_ciudades}")



###########################

'''
Retornar la suma de los habitantes de todas las ciudades.
'''

totalHabitantes = ListaCiudades.sumaTotalHabitantes()
print(f"La población total de todas las ciudades es: {totalHabitantes}")


###########################

'''
Añadir ciudad. Este método recibe un objeto ciudad como parámetro e
    intenta añadir esa ciudad a la lista. Si la ciudad está en la lista no podrá
    añadirla y retornará False. En caso de añadirla el retorno será True. Para
    comprobar si un valor está en una lista se puede utilizar:
        if valor in lista
        if valor not in lista

'''

# Crear una nueva ciudad
nueva_ciudad = Ciudad("Toronto", 3000000, "Canadá", "América")

# Intentar añadir la ciudad
if ListaCiudades.añadir_ciudad(nueva_ciudad):
    print("Ciudad añadida correctamente.")
else:
    print("La ciudad ya existe en la lista.")





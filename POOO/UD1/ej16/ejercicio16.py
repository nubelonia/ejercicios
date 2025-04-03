'''
Cada película (clase Movie) tiene los atributos: título, año, director, reparto, género,
minutos y productora.
Se trata de programar métodos que permitan:
    -Retornar las pelis de una productora pasada como parámetro.
    -Retornar las pelis con una cadena en el título. Esta cadena se pasará como
    parámetro.
    -Retornar cuántas pelis superan la duración media.
    -Ordenar por el campo duración. Para realizar esta tarea debemos utilizar lista.sort()
    y añadir a la clase Movie el método lt (less than) y en este programar cuando
    consideramos que una peli es menor que otra.

        def lt(self, otra):
            return self.minutes < otra.minutes

'''

######################

# Retornar las pelis de una productora pasada como parámetro.

from clase_ej16 import ListaPeliculas, Movie

productora_intro = input("Introduce productora: ")

peliculas = ListaPeliculas.pelisPorProductora(productora_intro)

if peliculas:
    print(f"Peliculas de la productora: {productora_intro}")
    for peliculas_productora in peliculas:
        print(peliculas_productora)

else:
    print(f"No se encontraron pelis de {productora_intro}")


# Retornar las pelis con una cadena en el título. Esta cadena se pasará como

cadenaTitulo_intro = input("Introduce cadena para Título de pelicula: ")
tituloPeliCadena = ListaPeliculas.pelisPorCadenaTitulo(cadenaTitulo_intro)

if cadenaTitulo_intro:
    print(f"Peliculas que contienen los caractéres {cadenaTitulo_intro}: ")
    for pelicula in tituloPeliCadena:
        print(pelicula)

else:
    print(f"No se encontró peliculas para los carácteres introducidos")


# Retornar cuántas pelis superan la duración media.

        # Obtener la cantidad total de películas
cantidadTotalPeliculas = ListaPeliculas.totalPeliculas()
print(f"Total de películas: {cantidadTotalPeliculas}")

        # Calcular la media de duración
mediaDuracion = ListaPeliculas.mediaDuracionPeliculas()
print(f"La media de duración de las películas es: {mediaDuracion:.2f} minutos")

        # Obtener películas que superan la media
peliculas_superan = ListaPeliculas.peliculasSuperanMedia()

        # Mostrar resultados
print(f"Películas que superan la duración media ({mediaDuracion:.2f} min):")
for pelicula in peliculas_superan:
    print(pelicula)

        # Obtener y mostrar la cantidad de películas que superan la media
cantidad_peliculas_superan = ListaPeliculas.cantidadPeliculasSuperanMedia()
print(f"Cantidad de películas que superan la duración media: {cantidad_peliculas_superan}")


        # Ordenamos las películas por duración
ListaPeliculas.ordenarPorDuracion()

        # Mostramos la lista ordenada
print("\n Películas ordenadas por duración:")
for pelicula in ListaPeliculas.list_movies:
    print(pelicula)


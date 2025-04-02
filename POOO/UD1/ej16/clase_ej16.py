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

class Movie:
    def __init__(self, titulo, año, director, reparto, genero, minutos, productora):
        self.titulo = titulo
        self.año = año
        self.director = director
        self.reparto = reparto
        self.genero = genero
        self.minutos = minutos
        self.productora = productora

    def __str__(self):
        return f"Titulo: {self.titulo} - Año: {self.año} - Director: {self.director} - Reparto: {self.reparto} - Género: {self.genero} - Duración: {self.minutos} minutos - Productora: {self.productora}" 




class ListaPeliculas:
        list_movies = [
            Movie("The Shawshank Redemption", 1994, "Frank Darabont", 
              "Tim Robbins, Morgan Freeman", "Drama", 142, "Castle Rock Entertainment"),
        
            Movie("The Godfather", 1972, "Francis Ford Coppola", 
              "Marlon Brando, Al Pacino", "Drama", 175, "Paramount Pictures"),
        
            Movie("The Dark Knight", 2008, "Christopher Nolan", 
              "Christian Bale, Heath Ledger", "Action", 152, "Warner Bros. Pictures"),
        
            Movie("The Lord of the Rings: The Return of the King", 2003, "Peter Jackson", 
              "Elijah Wood, Viggo Mortensen", "Adventure", 201, "New Line Cinema"),
        
            Movie("Pulp Fiction", 1994, "Quentin Tarantino", 
              "John Travolta, Uma Thurman", "Crime", 154, "Miramax Films"),
        
            Movie("Forrest Gump", 1994, "Robert Zemeckis", 
              "Tom Hanks, Robin Wright", "Drama", 142, "Paramount Pictures"),
        
            Movie("Inception", 2010, "Christopher Nolan", 
              "Leonardo DiCaprio, Joseph Gordon-Levitt", "Action", 148, "Warner Bros. Pictures"),
        
            Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", 
              "Keanu Reeves, Laurence Fishburne", "Action", 136, "Warner Bros. Pictures"),
        
            Movie("The Silence of the Lambs", 1991, "Jonathan Demme", 
              "Jodie Foster, Anthony Hopkins", "Crime", 118, "Orion Pictures"),
        
            Movie("The Departed", 2006, "Martin Scorsese", 
              "Leonardo DiCaprio, Matt Damon", "Crime", 151, "Warner Bros. Pictures"),
        
            Movie("The Prestige", 2006, "Christopher Nolan", 
              "Christian Bale, Hugh Jackman", "Drama", 130, "Warner Bros. Pictures"),
        
            Movie("The Green Mile", 1999, "Frank Darabont", 
              "Tom Hanks, Michael Clarke Duncan", "Drama", 189, "Castle Rock Entertainment"),
        
            Movie("The Godfather: Part II", 1974, "Francis Ford Coppola", 
              "Al Pacino, Robert De Niro", "Drama", 202, "Paramount Pictures"),
        
            Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", 
              "Elijah Wood, Ian McKellen", "Adventure", 178, "New Line Cinema"),
        
            Movie("The Lord of the Rings: The Two Towers", 2002, "Peter Jackson", 
              "Elijah Wood, Viggo Mortensen", "Adventure", 179, "New Line Cinema"),
        
            Movie("The Dark Knight Rises", 2012, "Christopher Nolan", 
              "Christian Bale, Tom Hardy", "Action", 164, "Warner Bros. Pictures"),
        
            Movie("One Flew Over the Cuckoo's Nest", 1975, "Milos Forman", 
              "Jack Nicholson, Louise Fletcher", "Drama", 133, "Fantasy Films"),
        
            Movie("Goodfellas", 1990, "Martin Scorsese", 
              "Robert De Niro, Ray Liotta", "Crime", 146, "Warner Bros. Pictures")
    ]
         

###############################

# Retornar las pelis de una productora pasada como parámetro.
         
        @classmethod
        def pelisPorProductora(cls, productora):
        #Vamos a filtrar las pelis según productora
            peliculas_productor = [peliculas for peliculas in cls.list_movies if peliculas.productora.lower() == productora.lower()]
            return peliculas_productor


# Retornar las pelis con una cadena en el título. Esta cadena se pasará como parámetro.

        @classmethod
        def pelisPorCadenaTitulo(cls, cadenaTitulo):
            peliculas_cadena = [pelicula for pelicula in cls.list_movies if cadenaTitulo.lower() in pelicula.titulo.lower()]
            return peliculas_cadena
        
# Retornar cuántas pelis superan la duración media.
        

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

class Ciudad:
    def __init__(self, nombre, poblacion, pais, continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.pais = pais
        self.continente = continente

    def __str__(self):
        return f"Nombre ciudad: {self.nombre} - Población: {self.poblacion} - Pais: {self.pais} - Continente: {self.continente}"
    
    def __eq__(self, otra_ciudad):
        return self.nombre == otra_ciudad.nombre and self.pais == otra_ciudad.pais
            
  
class ListaCiudades:

    list_cities = [Ciudad("Bogotá", 8000000, "Colombia", "América"),
Ciudad("Lima", 10000000, "Peru", "America"),
Ciudad("Paris", 5000000, "Francia", "Europa"),
Ciudad("Berlin", 4000000, "Alemania", "Europa"),
Ciudad("Tokio", 9000000, "Japón", "Asia"),
Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
Ciudad("Moscú", 10000000, "Rusia", "Europa"),
Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
Ciudad("Roma", 4000000, "Italia", "Europa"),
Ciudad("Pekín", 20000000, "China", "Asia"),
Ciudad("Delhi", 15000000, "India", "Asia"),
Ciudad("El Cairo", 7000000, "Egipto", "África"),
Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
Ciudad("Madrid", 6000000, "España", "Europa"),
Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
]
    
# Mostrar las ciudades de un continente dado.

    @classmethod
    def mostrar_ciudades_continente(cls, continente):
        # Vamos a filtrar las ciudades por continente creando una rastreo que devuelva una lista
        
        ciudades_encontradas = [ciudad for ciudad in cls.list_cities 
                                if ciudad.continente.lower() == continente.lower()]
        return ciudades_encontradas
    
# Mostrar las ciudades con una población mayor que un número dado.

    @classmethod
    def mostrar_por_población(cls, poblacion_introducida):

        ciudades_segun_poblacion = [ciudad for ciudad in cls.list_cities if ciudad.poblacion > poblacion_introducida ]
        return ciudades_segun_poblacion
    
# Retornar el número de ciudades de un país dado.

    @classmethod
    def mostrar_ciudades_pais(cls, pais_introducido):

        ciudades_por_pais = [ciudad for ciudad in cls.list_cities if ciudad.pais.lower() == pais_introducido.lower()]
        return ciudades_por_pais
    
# Retornar el número de ciudades que contienen una cadena en su nombre.

    @classmethod
    def contar_ciudades_cadena(cls, cadena):
        
        return sum(1 for ciudad in cls.list_cities if cadena.lower() in ciudad.nombre.lower())
        
    
# Retornar la media de la población de las ciudades de un país.

    @classmethod
    def media_poblacion_por_pais(cls, pais_buscado):
        ciudades_pais = [ciudad.poblacion for ciudad in cls.list_cities if ciudad.pais.lower() == pais_buscado.lower()]
        
        if not ciudades_pais:  # Si la lista está vacía
            return None
        
        media_poblacion = sum(ciudades_pais) / len(ciudades_pais)
        return media_poblacion


# Retornar una lista con las ciudades de un país.

    @classmethod
    def listaCiudades_pais(cls, pais_consultado):
        # Filtra las ciudades cuyo país coincide con el país ingresado (ignorando mayúsculas)
        listaCiudades_por_pais = [ciudad for ciudad in cls.list_cities if ciudad.pais.lower() == pais_consultado.lower()]
        return listaCiudades_por_pais

# Retornar la suma de los habitantes de todas las ciudades.

    @classmethod
    def sumaTotalHabitantes(cls):
        return sum(ciudad.poblacion for ciudad in cls.list_cities)
    
# Añadir ciudad

    @classmethod
    def añadir_ciudad(cls, nueva_ciudad):
        if nueva_ciudad in cls.list_cities:  # Verifica si la ciudad ya está en la lista
            return False  # Si ya existe, no se añade y retorna False
    
        cls.list_cities.append(nueva_ciudad)  # Si no está en la lista, la agrega
        return True  # Retorna True para indicar que se añadió correctamente



    

                                
        
        
            
  
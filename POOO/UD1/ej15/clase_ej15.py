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
            
  
class Lista_ciudades:

    list_cities = [1, 
Ciudad("Bogotá", 8000000, "Colombia", "América"),
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
    def mostrar_ciudades_continente(cls, ciudad_buscada):
        for ciudad in list_ 
  
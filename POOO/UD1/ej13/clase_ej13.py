'''
Para este ejercicio utilizaremos la lista de productos vista antes. 
Accederemos al primer objeto de la lista y le añadiremos el atributo
caducado con el valor True. Recorremos la lista y visualizamos 
el atributo dict de cada objeto. Recuerda que este atributo proporciona
información sobre los atributos de un objeto, en forma de diccionario.

'''
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        
    #Transformamos a cada cadena string
    def __str__(self):
        return f"Nombre: {self.nombre} - categoria: {self.categoria} - precio: {self.precio} - cantidad: {self.cantidad}"
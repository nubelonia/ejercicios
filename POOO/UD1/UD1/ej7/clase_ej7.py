'''
Obtener la media de los precios 
de los productos de la categoría ‘verdura’.
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
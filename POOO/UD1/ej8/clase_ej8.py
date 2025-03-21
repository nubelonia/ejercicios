'''
Contar cuántos productos tienen un precio 
entre 2 y 3 (excluidos).
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
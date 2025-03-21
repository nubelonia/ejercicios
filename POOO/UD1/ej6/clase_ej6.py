'''
6. Visualizar en pantalla aquellos productos cuyo precio esté entre 1.5 y 2.5 (incluidos).
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
'''
Calcular la media de todos los precios de los productos.

'''
class Producto:
    contador_producto = 0
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        Producto.contador_producto += 1
        
    #Transformamos a cada cadena string
    def __str__(self):
        return f"Nombre: {self.nombre} - categoria: {self.categoria} - precio: {self.precio} - cantidad: {self.cantidad}"
    #Método de clase para que me de el contador en entero
    #No es necesario para este ejercicio pero lo añadí para hacerlo invocando al
    #método de clase total_productos()
    
    @classmethod
    def total_productos(cls):
        return cls.contador_producto 


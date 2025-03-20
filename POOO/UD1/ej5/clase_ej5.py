'''
5. Visualizar en pantalla aquellos productos que pertenezcan a la categoría ‘verdura’.

'''

class Producto:

    contador_producto = 0 

    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        Producto.contador_producto += 1

    @classmethod
    def metodo_contador_producto(cls):
        print (f"En total hay {cls.contador_producto} productos")

    '''
    Para hacer el filtrado de los productos, hago uso del 
    metodo __str__ que lo que hace es convertir los objetos de clase
    Producto en cadena de texto
    '''

    def __str__(self):
        
        return f"Categoria-producto: {self.categoria} - Nombre: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"
        
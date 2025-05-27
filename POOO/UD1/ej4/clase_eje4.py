'''
4. Modificar la clase “Producto” del ejercicio anterior añadiendo un método que
actualice la cantidad de un producto sumándole un valor pasado como parámetro.
Mostrar los datos de un producto antes y después de ser modificada su cantidad.

'''
class Producto:

    contador_producto = 0 #Agregamos este atributo de clase

    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        #atributo contador_producto (suma 1, cada vez que se crea un objeto)
        Producto.contador_producto += 1

    # Hay que añadir un método de clase para invocar el atributo de clase    

    @classmethod
    def metodo_contador_producto(cls):
        print (f"En total hay {cls.contador_producto} productos")
    



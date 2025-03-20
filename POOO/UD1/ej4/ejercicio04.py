'''
4. Modificar la clase “Producto” del ejercicio anterior añadiendo un método que
actualice la cantidad de un producto sumándole un valor pasado como parámetro.
Mostrar los datos de un producto antes y después de ser modificada su cantidad.

'''

from clase_eje4 import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]

#Llamo al metodo de clase metodo_contador_producto() desde su clase Producto e imprimo
print(Producto.metodo_contador_producto())

'''
En total hay 5 productos
'''


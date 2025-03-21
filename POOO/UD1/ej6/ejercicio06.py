'''
6. Visualizar en pantalla aquellos productos cuyo precio esté entre 1.5 y 2.5 (incluidos).
'''

from clase_ej6 import Producto

#Esto es una lista de objetos (en este caso de la clase Producto)
productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]


for producto in productos:
    if producto.precio >=1.5 and producto.precio <= 2.5:
        print(producto)

    
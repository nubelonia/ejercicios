'''
Contar cuántos productos tienen un precio 
entre 2 y 3 (excluidos).
'''

from clase_ej8 import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]

for producto in productos:
    if producto.precio > 2 and producto.precio < 3:
        print(producto)

        

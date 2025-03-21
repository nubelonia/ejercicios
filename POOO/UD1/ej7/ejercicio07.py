'''
Obtener la media de los precios 
de los productos de la categoría ‘verdura’.
'''

from clase_ej7 import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]


# obtener la media de los precios de las verduras
sumatorio_precios = 0
contador_verduras = 0
for producto in productos:
    # preguntamos si el producto es una verdura
    # en caso afirmativo sumamos el precio del producto
    # y aumentamos el contador de verduras
    if producto.categoria.lower() == "verdura":
        sumatorio_precios += producto.precio
        contador_verduras += 1
# al final del bucle calculamos la media
media = sumatorio_precios / contador_verduras
print(f"La media de los precios de las verduras es {media}")  


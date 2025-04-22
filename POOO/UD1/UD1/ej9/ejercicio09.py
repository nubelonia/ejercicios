'''
Calcular la media de todos los precios de los productos.

'''
from clase_ej9 import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]


sumatorio_precio = 0

#Comento otra alternativa de hacerlo, aunque asi es más adecuado
# cantidad_total_productos = Producto.total_productos()
for producto in productos:
    sumatorio_precio += producto.precio

#media = sumatorio_precio / cantidad_total_productos

media = sumatorio_precio / len(productos)

print(f"La media de los precios para todos los productos es: {media}")








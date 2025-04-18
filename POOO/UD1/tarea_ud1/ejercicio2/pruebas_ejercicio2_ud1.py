from clases_ejercicio2_ud1 import *

# - Llama al método “listado” y muestra los productos existentes.

GestionAlmacen.listado()


# - Usando el método “nuevo_producto”, añade dos productos nuevos. El segundo debe tener 
# el mismo identificador que el primero. Comprueba si se añaden los dos o uno solo.

p6 = Producto(6, "Koipe", "Aceites", 5.50, 40, 30)
p7 = Producto(5, "El ventero", "Quesos", 4.50, 50, 30)

GestionAlmacen.nuevo_producto(p6)
GestionAlmacen.nuevo_producto(p7) #Aquí salta la duplicación del id

# Imprimo de nuevo el listado con el producto añadido
GestionAlmacen.listado()



# - Llama al método “bajo_mínimos” y guarda en una lista los productos que estén en mínimos.
#  Muestra el contenido de la lista.

print("PRODUCTOS DEBAJO DE STOCK MÍNIMO")
productos_minimos = GestionAlmacen.bajo_minimos()
if productos_minimos:
    for producto in productos_minimos:
        print(producto)
else:
    print("No hay productos por debajo del stock mínimo.")


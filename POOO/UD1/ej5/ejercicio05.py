
'''
5. Visualizar en pantalla aquellos productos que pertenezcan a la categoría ‘verdura’.

'''

from clase_ej5 import Producto

#Esto es una lista de objetos (en este caso de la clase Producto)
productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]

'''
El ejercicio pide que filtremos de todos los productos creados
los que sean de categoría verdura. Explico como:
producto_categoria = [producto for producto in productos if
                      producto.categoria.lower() == "verdura"]
linea 17 .- Filtra los productos de la lista productos de arriba, y
guarda en producto_categoria los que son de la categoria "verdura".
Explicación paso a paso:
1º 
* productos_verdura = [...]
Esto crea una nueva lista llamada "productos_verdura"
Dentro de los corchetes [...] vamos a construir la lista de manera
dinamica usando "lista por comprensión"
2º
producto for producto in productos
* producto --> Es una variable temporal que representa cada elemento
de la lista productos.
* for producto in productos --> Hace un recorrido en la lista productos.
Ejemplo: 
Si productos tiene estos valores:
productos = [
    Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50)
]
Entonces, el for recorrerá cada objeto uno por uno:
producto = Producto("tomate", "fruta", 2.3, 100)
producto = Producto("patata", "verdura", 1.5, 200)
producto = Producto("cebolla", "verdura", 1.8, 150)
producto = Producto("manzana", "fruta", 3.2, 50)
3º 
* if producto.categoria.lower() == "verdura"
Aqui usa el condicional para filtrar los productos:
* producto.categoria --> Obtiene la categoría del producto
* .lower() --> Convierte la categoría a minúsculas (para evitar errores
si hay mayúsculas)
* == "verdura" --> Comprueba si la categoría es exactamente "verdura"
Explicación de las iteraciones:
Explicación con ejemplo práctico
Vamos a ver qué pasa paso a paso en el código con los productos de ejemplo:
🔍 Iteración 1:
    producto = Producto("tomate", "fruta", 2.3, 100)
    producto.categoria.lower() → "fruta"
    "fruta" == "verdura" ❌ (No es verdura, se ignora)
🔍 Iteración 2:
    producto = Producto("patata", "verdura", 1.5, 200)
    producto.categoria.lower() → "verdura"
    "verdura" == "verdura" ✅ (Se añade a productos_verdura)
🔍 Iteración 3:
    producto = Producto("cebolla", "verdura", 1.8, 150)
    producto.categoria.lower() → "verdura"
    "verdura" == "verdura" ✅ (Se añade a productos_verdura)
🔍 Iteración 4:
    producto = Producto("manzana", "fruta", 3.2, 50)
    producto.categoria.lower() → "fruta"
    "fruta" == "verdura" ❌ (No es verdura, se ignora)
    Resultado.-
    productos_verdura = [
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150)
]
'''
#Ojo podemos saltarnos esta linea de código, pero la diferencia es
#que no lo almacenará, y solo lo imprime. Ya según el caso.
productos_verdura = [producto for producto in productos if producto.categoria.lower() == "verdura"]
for producto in productos:
    if producto.categoria.lower() == "verdura":
        print(producto)

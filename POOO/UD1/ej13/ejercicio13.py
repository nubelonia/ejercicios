'''
Para este ejercicio utilizaremos la lista de productos vista antes. 
Accederemos al primer objeto de la lista y le añadiremos el atributo
 caducado con el valor True. Recorremos la lista y visualizamos 
 el atributo dict de cada objeto. Recuerda que este atributo proporciona
   información sobre los atributos de un objeto, en forma de diccionario.

'''
from clase_ej13 import Producto

# Crear lista de productos
productos = [
    Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75)
]

'''
En Python, puedes agregar atributos dinámicamente a los objetos, 
aunque no estén definidos en __init__. Esto solo afecta a ese 
objeto en particular y no a toda la clase.

Se agrega un nuevo atributo solamente a ese objeto (no afecta a los demás 
productos).

'''
# Añadir un atributo "caducado" al primer producto de la lista
productos[0].caducado = True  

'''
producto.__dict__ → Es un diccionario que muestra los atributos de cada objeto.
El for recorre la lista e imprime los atributos de cada producto 
en formato diccionario.
'''

# Recorrer la lista e imprimir los atributos de cada objeto como diccionario
for producto in productos:
    print(producto.__dict__)  
    





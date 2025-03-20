'''
3. Diseñar una clase Python llamada “Producto” con los atributos nombre, categoría,
precio y cantidad. Diseña en esta clase el método __str__ de forma que retorne
todos los atributos en un dato de tipo cadena (str).
Crear dos productos pertenecientes a esa clase y mostrar todos los datos de aquel
producto que tenga mayor precio.

'''

from clase_ej3 import Producto

p1 = Producto("Tomate", "Verdura", 1.2, 20)
p2 = Producto("Manzana", "Fruta", 2, 30)


#En este caso usamos if else, para comparar los dos productos. como se cumple la primera condición, pues la imprime.
if p2.precio > p1.precio:
    print("El producto más caro es: ", p2)
else:
    print("El producto más caro es: ", p1)

'''
El producto más caro es:  Nombre: Manzana, Categoria: Fruta, Precio: 2, Cantidad: 30

'''
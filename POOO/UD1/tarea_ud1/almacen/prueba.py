from almacen import Producto, GestionAlmacen

GestionAlmacen.listado()

p = Producto(10, "Nescafé", "Café", 3.50, 10, 15)
GestionAlmacen.nuevo_producto(p)
GestionAlmacen.listado()

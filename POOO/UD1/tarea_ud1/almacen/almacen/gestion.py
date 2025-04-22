from .producto import Producto

class GestionAlmacen:
    
    # Atributo de clase (lista para guardar productos)
    lista_productos = [Producto(1, "Pepsi", "Refrescos", 1.50, 30, 20), 
                       Producto(2, "Pascual", "Leche", 1.20, 20, 40),
                       Producto(3, "Don Simon", "Zumos", 1.30, 30, 30),
                       Producto(4, "Cruzcampo", "Cervezas", 1.50, 60, 40),
                       Producto(5, "El ventero", "Quesos", 4.50, 50, 30)
                       ]
    
    # Métodos

    '''
    buscar_por_id. Recibe un identificador de producto como argumento y lo busca en la lista. 
    En caso de encontrarlo lo retorna, si no lo encuentra debe retornar el valor None
    '''
    # En primer lugar creo el metodo buscar_por_id, para comprobar si ya existe el producto. 

    @classmethod
    def buscar_por_id(cls, id):
        for producto in cls.lista_productos:
            if producto.id == id:
                return producto
        return None

    
    '''
    Recibe datos de un producto como argumentos y lo añade a la lista, siempre y cuando 
    su identificador no exista en la misma. RetornaTrue si el producto se añadió a la lista, 
    False en caso contrario
    '''    
    @classmethod
    def nuevo_producto(cls, producto):
        if cls.buscar_por_id(producto.id):
            print(f"No se puede añadir el producto. Ya existe éste producto con id: {producto.id}" )
            return False
        else:
            cls.lista_productos.append(producto)
            print(f"El producto con id: {producto.id} se ha añadido satisfactoriamente")
            return True


    
    # bajo_minimos. Retorna una lista con los productos que estén bajo mínimos.
    @classmethod
    def bajo_minimos(cls):
        productos_bajo_minimos = []
        for producto in cls.lista_productos:
            if producto.stock < producto.stock_minimo:
                productos_bajo_minimos.append(producto)
        
        return productos_bajo_minimos
    
    
    
    
    # listado. Muestra en pantalla un listado de los productos existentes en el almacén.
    @classmethod
    def listado(cls):
        print(f"LISTADO DE PRODUCTOS")
        print(*cls.lista_productos, sep="\n")

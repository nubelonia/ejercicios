class Producto:
    def __init__(self,  id, nombre, categoria, precio, stock, stock_minimo):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

      

    
    # Métodos exigidos

    # actualizar_stock. Recibe como argumento un número de unidades y las
    # sumará al stock existente.
    def actualizar_stock(self, unidades):
        self.stock += unidades

    




    # esta_en_minimos. Retorna True si el stock del producto es inferior al stock
    # mínimo, False en caso contrario.

    def esta_en_minimos(self):
        if self.stock < self.stock_minimo:
            return True
        else:
            return False





    # Define el método mágico que creas conveniente para mostrar el identificador,
    # nombre y stock del producto.

    def __str__(self):
        return f"Id: {self.id}, Nombre-producto: {self.nombre}, stock: {self.stock}"





    # Define el método mágico que consideres oportuno para determinar si dos productos son iguales.
    # Se consideran iguales dos productos si tienen el mismo identificador

    def __eq__(self, otro_id):
        return self.id == otro_id
        
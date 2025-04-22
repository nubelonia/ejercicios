class Producto:
    def __init__(self,  id, nombre, categoria, precio, stock, stock_minimo):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo
       
    def actualizar_stock(self, unidades):
        self.stock += unidades
    
    def esta_en_minimos(self):
        if self.stock < self.stock_minimo:
            return True
        else:
            return False

    def __str__(self):
        return f"Id: {self.id}, Nombre-producto: {self.nombre}, stock: {self.stock}"
       
    def __eq__(self, otro_id):
        return self.id == otro_id
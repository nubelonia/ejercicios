from clases import BikestoreDB

app = BikestoreDB(user='bikestore_user', password='bikestore_pass')  

print("Ejecutando pruebas.py...")

# Listar productos
print("Llamando a listar_productos()")
app.listar_productos()

# Listar clientes de una ciudad
print("Llamando a listar_clientes_por_ciudad('Madrid')")
app.listar_clientes_por_ciudad("Madrid")

# Actualizar email
print("Llamando a actualizar_email_cliente(1, 'nuevo@email.com')")
app.actualizar_email_cliente(1, "nuevo@email.com")

# Insertar marca
print("Llamando a insertar_marca('Nueva Marca')")
app.insertar_marca("Nueva Marca")


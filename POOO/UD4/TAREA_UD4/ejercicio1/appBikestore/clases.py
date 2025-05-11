import mysql.connector
from mysql.connector import Error

class BikestoreDB:
    def __init__(self, host='localhost', database='bikestore', user='bikestore_user', password='bikestore_pass'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def conectar(self):
        print("Intentando conectar a la base de datos...")
        
        try:
            conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                                
        )
            print("Conexión exitosa.")
            return conn
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None



    def listar_productos(self):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                print("Conexión a la base de datos establecida.")  # Confirmar conexión
                query = "SELECT * FROM products"
                print(f"Ejecutando consulta: {query}")  # Mostrar la consulta
                cursor.execute(query)
                resultados = cursor.fetchall()
                print("Resultados obtenidos de la consulta:", resultados)  # Mostrar los resultados crudos
                if resultados:
                    print(f"Cantidad de productos encontrados: {len(resultados)}")
                    for fila in resultados:
                        print(fila)
                else:
                    print("No se encontraron productos en la tabla 'products'.")
            except mysql.connector.Error as err:
                print(f"Error al ejecutar la consulta: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")





    def listar_clientes_por_ciudad(self, ciudad):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers WHERE city = %s", (ciudad,))
                clientes = cursor.fetchall()
                if clientes:
                    for cliente in clientes:
                        print(cliente)
                else:
                    print(f"No se encontraron clientes en la ciudad: {ciudad}")
            except Error as e:
                print(f"Error al listar clientes por ciudad: {e}")
            finally:
                cursor.close()
                conn.close()

    def actualizar_email_cliente(self, customer_id, nuevo_email):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE customers SET email = %s WHERE customer_id = %s", (nuevo_email, customer_id))
                conn.commit()
                if cursor.rowcount > 0:
                    print(f"{cursor.rowcount} fila(s) actualizada(s).")
                else:
                    print("No se encontró ningún cliente con ese ID.")
            except Error as e:
                print(f"Error al actualizar email del cliente: {e}")
            finally:
                cursor.close()
                conn.close()

    def insertar_marca(self, nombre_marca):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO brands (brand_name) VALUES (%s)", (nombre_marca,))
                conn.commit()
                print("Marca insertada correctamente.")
            except Error as e:
                print(f"Error al insertar marca: {e}")
            finally:
                cursor.close()
                conn.close()

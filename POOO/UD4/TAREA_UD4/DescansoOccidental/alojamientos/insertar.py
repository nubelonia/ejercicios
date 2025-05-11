import os
import sys
import django

# Agregar la ruta del proyecto al sistema
sys.path.append("c:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/TAREA_UD4/DescansoOccidental")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DescansoOccidental.settings')
django.setup()

from alojamientos.models import Hotel

# Lista de hoteles a insertar
hoteles = [
    {"nombre": "Hotel Pepito", "categoria": "4 estrellas", "direccion": "Av. Principal 123", "telefono": "123456789", "correo_electronico": "central@hotel.com", "ano_creacion": 1995, "numero_habitaciones": 50},
    {"nombre": "Hotel Paraíso", "categoria": "5 estrellas", "direccion": "Calle Paraíso 45", "telefono": "987654321", "correo_electronico": "paraiso@hotel.com", "ano_creacion": 2000, "numero_habitaciones": 120},
    {"nombre": "Hotel Sol", "categoria": "3 estrellas", "direccion": "Plaza del Sol 67", "telefono": "1122334455", "correo_electronico": "sol@hotel.com", "ano_creacion": 2010, "numero_habitaciones": 80},
    {"nombre": "Hotel Luna", "categoria": "4 estrellas", "direccion": "Calle Luna 89", "telefono": "5566778899", "correo_electronico": "luna@hotel.com", "ano_creacion": 2005, "numero_habitaciones": 60},
    {"nombre": "Hotel Maravilla", "categoria": "5 estrellas", "direccion": "Av. Playa 101", "telefono": "6677889900", "correo_electronico": "maravilla@hotel.com", "ano_creacion": 2018, "numero_habitaciones": 150},
    {"nombre": "Hotel Relajate", "categoria": "4 estrellas", "direccion": "Calle Relax 202", "telefono": "4455667788", "correo_electronico": "relax@hotel.com", "ano_creacion": 1998, "numero_habitaciones": 90},
    {"nombre": "Hotel Vistas", "categoria": "3 estrellas", "direccion": "Vista al Mar 303", "telefono": "7788990011", "correo_electronico": "vista@hotel.com", "ano_creacion": 2012, "numero_habitaciones": 70},
    {"nombre": "Hotel Montaña", "categoria": "5 estrellas", "direccion": "Calle Montaña 404", "telefono": "8899001122", "correo_electronico": "montana@hotel.com", "ano_creacion": 2008, "numero_habitaciones": 140},
    {"nombre": "Hotel Urbano", "categoria": "3 estrellas", "direccion": "Av. Ciudad 505", "telefono": "9900112233", "correo_electronico": "urbano@hotel.com", "ano_creacion": 1990, "numero_habitaciones": 100},
    {"nombre": "Hotel Esplendor", "categoria": "4 estrellas", "direccion": "Boulevard Esplendor 606", "telefono": "1100223344", "correo_electronico": "esplendor@hotel.com", "ano_creacion": 2015, "numero_habitaciones": 110},
]

# Insertar los hoteles en la base de datos
for hotel in hoteles:
    hotel = Hotel(**hotel)
    hotel.save()
    print(f"Hotel {hotel.nombre} guardado en la base de datos")
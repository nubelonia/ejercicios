import os
import sys
import django

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

personas = [
    Persona(nombre='Juan', telefono='123456789', correo='juan@gmail.com'),
    Persona(nombre='Ana', telefono='987654321', correo='ana@gmail.com'),
    Persona(nombre='Pedro', telefono='456789123', correo='peter@pan.es'),
    Persona(nombre='María', telefono='654987321', correo='maria@cuetara.es'),
    Persona(nombre='Luis', telefono='789123456', correo='luis@ito.es'),
]

for persona in personas:
    persona.save()
    print(f"Persona {persona.nombre} guardada en la base de datos")
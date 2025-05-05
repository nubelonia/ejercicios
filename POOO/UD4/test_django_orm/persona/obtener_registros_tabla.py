import os
import sys
import django

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

# Obtener todas las instancias de la clase Persona
personas = Persona.objects.all()

# Mostrar las instancias de la clase Persona
for persona in personas:
    print(persona)
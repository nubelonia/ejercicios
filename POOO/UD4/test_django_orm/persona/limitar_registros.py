import os
import sys
import django

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

# Limitar la cantidad de registros a obtener. 
# En este caso solo muestra los tres primeros.
personas = Persona.objects.all()[:3]

for persona in personas:
    print(persona)
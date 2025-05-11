import os
import sys
import django

# Agregar la ruta del proyecto al sistema
sys.path.append("c:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/TAREA_UD4/DescansoOccidental")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DescansoOccidental.settings')
django.setup()

from alojamientos.models import Hotel

# Obtener todas las instancias de la clase Persona
hoteles = Hotel.objects.all()

# Mostrar las instancias de la clase Persona
for hotel in hoteles:
    print(hotel)
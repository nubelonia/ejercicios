import os
import sys
import django

# Agregar la ruta del proyecto al sistema
sys.path.append("c:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/TAREA_UD4/DescansoOccidental")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DescansoOccidental.settings')
django.setup()

from alojamientos.models import Hotel

# Filtrar por nombre
hoteles = Hotel.objects.filter(categoria='5 estrellas')

for hotel in hoteles:
    print(hotel)
from django.shortcuts import render
from .models import Evento
from datetime import date

def index(request):
    return render(request, 'index.html')

def eventos_list(request):
    eventos = Evento.objects.all().order_by('fecha')
    return render(request, 'list.html', {'eventos': eventos, 'titulo': 'EventosYa. Todos los eventos'})

def eventos_pasados(request):
    eventos = Evento.objects.filter(fecha__lt=date.today()).order_by('fecha')
    return render(request, 'list.html', {'eventos': eventos, 'titulo': 'EventosYa. Eventos pasados'})

def eventos_festivales(request):
    eventos = Evento.objects.filter(nombre__icontains='Festival').order_by('fecha')
    return render(request, 'list.html', {'eventos': eventos, 'titulo': 'EventosYa. Festivales'})

def creator(request):
    creador = {"nombre": "Manu django web", "correo": "manu@mail.com"}
    return render(request, 'creator.html', creador)

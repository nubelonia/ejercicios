from django.urls import path
from eventos import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('eventos/list/', view=views.eventos_list, name='eventos-list'),
    path('list/', view=views.eventos_list),
    path('eventos/pasados/', view=views.eventos_pasados, name='eventos-pasados'),
    path('eventos/festivales/', view=views.eventos_festivales, name='eventos-festivales'),
    path('eventos/creator', view=views.creator, name='eventos-creator'),
]

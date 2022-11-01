from django.urls import path
from . import views

urlpatterns = [
    path('grados/', views.grados, name='grados'),
    path('materias/<id_grado>/', views.materias_grados, name='materias_grados'),
    path('temas/<id_materia>/', views.temas_materia, name='temas_materia'),
    path('subtemas/<id_temas>/', views.sub_temas_materia, name='sub_temas_materia'),
    path('recursos/<id_sub_temas>/', views.recursos_sub_temas, name='recursos_sub_temas'),
]
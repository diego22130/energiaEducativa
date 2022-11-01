import re
from django.shortcuts import render
from .models import Grados, Materias, TemasMaterias, SubTemasMateria, Recursos
# Create your views here.

def grados(request):
    grados = Grados.objects.all()

    data = {
        'grados':grados,
    }

    return render(request, 'recursos/grados.html', data)


def materias_grados(request, id_grado):
    materias = Materias.objects.filter(grado=id_grado)
    

    data = {
        'materias':materias,
    }
    return render(request, 'materias/materias.html', data)

def temas_materia(request, id_materia):
    temas = TemasMaterias.objects.filter(materia=id_materia)
    data = {
        'temas':temas,
    }
    return render(request, 'materias/temas.html', data)

def sub_temas_materia(request, id_temas):
    subTemas = SubTemasMateria.objects.filter(temasMateria=id_temas)

    data = {
        'subTemas':subTemas,
    }

    return render(request, 'materias/subtemas.html', data)

def recursos_sub_temas(request, id_sub_temas):
    recursos = Recursos.objects.filter(subTemasMateria=id_sub_temas)

    data = {
        'recursos':recursos,
    }

    return render(request, 'recursos/recursosSubTemas.html', data)

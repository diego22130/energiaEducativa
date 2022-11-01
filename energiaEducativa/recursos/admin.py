from django.contrib import admin
from .models import Grados, Materias, TemasMaterias, SubTemasMateria, Recursos

class MateriasAdmin(admin.ModelAdmin):
    list_display = ['nomMateria', 'grado']

class RecursosAdmin(admin.ModelAdmin):
    list_display = ['tituloRecursos', 'subTemasMateria']

class SubTemasAdmin(admin.ModelAdmin):
    list_display = ['nomSubTema', 'temasMateria']

class TemasAdmin(admin.ModelAdmin):
    list_display = ['nomTema', 'materia']

# Register your models here.

admin.site.register(Grados)
admin.site.register(Materias, MateriasAdmin)
admin.site.register(TemasMaterias, TemasAdmin)
admin.site.register(SubTemasMateria, SubTemasAdmin)
admin.site.register(Recursos, RecursosAdmin)
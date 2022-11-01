from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Grados(models.Model):
    nomGrado = models.CharField(max_length=100)
    imgGrado = models.ImageField(upload_to='grados')

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'

    def __str__(self):
        return self.nomGrado

class Materias(models.Model):
    nomMateria = models.CharField(max_length=100)
    imgMateria = models.ImageField(upload_to='materias', default='img/educa.png')
    grado = models.ForeignKey(Grados, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return f'{self.nomMateria} - {self.grado}'

class TemasMaterias(models.Model):
    nomTema = models.CharField(max_length=255)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Temas Materia'
        verbose_name_plural = 'Temas Materia'

    def __str__(self):
        return f'{self.nomTema} {self.materia.grado}'

class SubTemasMateria(models.Model):
    nomSubTema = models.CharField(max_length=255)
    temasMateria = models.ForeignKey(TemasMaterias, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sub Temas Materia'
        verbose_name_plural = 'Sub Temas Materia'

    def __str__(self):
        return self.nomSubTema

class Recursos(models.Model):   
    tituloRecursos = models.CharField(max_length=255)
    descripcionRecursos = models.TextField(null=True, blank=True)
    linkRecursos = models.URLField()
    subTemasMateria = models.ForeignKey(SubTemasMateria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.tituloRecursos


    


    
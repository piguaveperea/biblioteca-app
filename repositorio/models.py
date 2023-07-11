from django.db import models
from biblioteca.models import Campus, Area
# Create your models here.

class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=40, unique=True)


class Tesis(models.Model):
    campus = models.ForeignKey(Campus, to_field='codigo', on_delete=models.CASCADE)
    area  = models.ForeignKey(Area, to_field='codigo', on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, to_field='codigo', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=200)
    n_clasificacion = models.CharField(max_length=10)
    cute = models.CharField(max_length=10)
    tema = models.CharField(max_length=200)
    autor = models.CharField(max_length=20)
    tutor = models.CharField(max_length=60)
    fecha =models.DateField()
    codigo_barra = models.CharField(max_length=200)


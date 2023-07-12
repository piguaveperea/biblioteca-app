from django.db import models
from biblioteca.models import Campus, Libro
# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=20, unique=True)

class Registro_Servicio(models.Model):
    servicio = models.ForeignKey(Servicio, to_field='codigo', on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, to_field='codigo', on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, to_field='codigo_barra', on_delete=models.CASCADE)
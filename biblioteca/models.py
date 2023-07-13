from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.


class Campus(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    codigo = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'campus',
        verbose_name_plural ='campus'

    def __str__ (self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre
    
class Area(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    numero = models.IntegerField()
    nombre_libro = models.CharField(max_length=250)
    codigo_barra = models.CharField(max_length=20, unique=True)
    n_clasificacion = models.CharField(max_length=10)
    area = models.ForeignKey(Area, to_field='codigo', on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, to_field='codigo', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, to_field='codigo', on_delete=models.CASCADE)
    cute = models.CharField(max_length=20)
    isbn = models.CharField(max_length=40)
    autor = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    fecha = models.PositiveIntegerField(validators=[MaxValueValidator(datetime.now().year), MinValueValidator(1600)], help_text="El formato correcto es YYYY")
    portada = models.ImageField(null=True, editable=True)

    class Meta:
        ordering = ['id']


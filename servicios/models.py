from django.db import models
from biblioteca.models import Campus
# Create your models here.




class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Registro_Servicio(models.Model):
    servicio = models.ForeignKey(Servicio, to_field='codigo', on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, to_field='codigo', on_delete=models.CASCADE)
    c_estudiante = models.IntegerField()
    fecha = models.DateField()
    
    class Meta:
        verbose_name = 'Registros de Servicios'
        verbose_name_plural = 'Registros de Servicios'
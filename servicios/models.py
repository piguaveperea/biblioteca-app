from django.db import models

# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=20, unique=True)



from django.contrib import admin
from .models import Libro, Campus, Categoria, Area
from . forms import LibroForm


class  AdminLibro(admin.ModelAdmin):
    list_display = ['numero', 'campus', 'area', 'n_clasificacion', 'cute', 'nombre_libro', 'categoria', 'autor', 'editorial', 'pais', 'fecha', 'codigo_barra', 'portada']
    list_editable = ['portada']
    form = LibroForm
    
# Register your models here.




admin.site.register(Libro, AdminLibro)
admin.site.register(Campus)
admin.site.register(Categoria)
admin.site.register(Area)


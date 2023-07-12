from django.contrib import admin
from .models import Libro, Campus, Categoria, Area
from . forms import LibroForm


class  AdminLibro(admin.ModelAdmin):
    list_display = ['numero', 'nombre_libro','isbn', 'codigo_barra', 'autor','categoria', 'area', 'campus', 'pais', 'editorial', 'portada']
    list_editable = ['portada']
    form = LibroForm
    
# Register your models here.




admin.site.register(Libro, AdminLibro)
admin.site.register(Campus)
admin.site.register(Categoria)
admin.site.register(Area)


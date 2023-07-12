from django.contrib import admin
from .models import Facultad, Tesis
# Register your models here.

class TesisAdmin(admin.ModelAdmin):
    list_display = ['campus', 'facultad' , 'area', 'n_clasificacion', 'cute', 'tema', 'autor', 'tutor','fecha', 'codigo_barra']
    pass

admin.site.register(Facultad)
admin.site.register(Tesis, TesisAdmin)

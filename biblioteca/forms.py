from django.forms import ModelForm
from .models import Libro
class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['numero', 'campus', 'area', 'n_clasificacion', 'cute', 'nombre_libro', 'categoria', 'autor', 'editorial', 'pais', 'fecha', 'codigo_barra']
        labels = {
            'fecha': 'Año',
            'n_clasificacion': 'Numero de Clasificación',
        }

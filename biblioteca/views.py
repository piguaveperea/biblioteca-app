from django.shortcuts import render
from .models import Libro
# Create your views here.

def buscar_libro(request):
    buscar_libro = request.GET.get('buscar_libro')
    if buscar_libro:
        libros = Libro.objects.filter(nombre_libro__icontains=buscar_libro)
    return render(request, 'index.html', {'libros': libros })
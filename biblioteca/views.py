from django.shortcuts import render
from .models import Libro

# Create your views here.

def index(request):
    return render(request, 'index.html')

def buscar_libro(request):
    buscar = request.GET.get('buscar_libro')
    if buscar:
        libros = Libro.objects.filter(nombre_libro__icontains = buscar)
    return render(request, 'index.html', {'libros': libros}) 
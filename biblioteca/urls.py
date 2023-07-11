from django.urls import path
from .views import buscar_libro

urlpatterns = [
    path('buscar_libro', view=buscar_libro, name='buscar_libro'),
]
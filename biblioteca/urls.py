from django.urls import path
from .views import index, buscar_libro

urlpatterns = [
    path('', view=index, name='index'),
    path('buscar_libro', view= buscar_libro, name='buscar_libro')
]
from django.contrib import admin
from .models import Servicio, Registro_Servicio
from rangefilter.filters import DateRangeFilterBuilder
# Register your models here.


class AdminRegistroServicio(admin.ModelAdmin):
    list_display = ['c_estudiante', 'campus', 'servicio', 'fecha']
    list_filter=[
        ('fecha', DateRangeFilterBuilder()),
    ]

admin.site.register(Servicio)
admin.site.register(Registro_Servicio, AdminRegistroServicio)
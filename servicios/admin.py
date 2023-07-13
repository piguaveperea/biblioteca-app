from django.contrib import admin
from .models import Servicio, Registro_Servicio
from rangefilter.filters import DateRangeFilterBuilder
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AdminRegistroServicio(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','c_estudiante', 'campus', 'servicio', 'fecha']
    list_filter=[
        ('fecha', DateRangeFilterBuilder()),
    ]

admin.site.register(Servicio)
admin.site.register(Registro_Servicio, AdminRegistroServicio)
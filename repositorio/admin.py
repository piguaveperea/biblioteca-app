from django.contrib import admin
from .models import Facultad, Tesis
# Register your models here.

class TesisAdmin(admin.ModelAdmin):
    list_display=['titulo', 'autor', 'tutor']

admin.site.register(Facultad)
admin.site.register(Tesis)

from django.contrib import admin
from .models import Tarea
# Register your models here.

class Tareacreadawhen(admin.ModelAdmin):
    readonly_fields = ("creado", )

admin.site.register(Tarea, Tareacreadawhen)
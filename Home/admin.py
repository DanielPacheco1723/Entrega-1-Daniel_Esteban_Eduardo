from django.contrib import admin

from .models import Estudiantes, Materias, Profesores

admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Materias)

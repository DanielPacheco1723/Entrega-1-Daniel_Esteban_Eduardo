from __future__ import unicode_literals
from django.db import models

class Estudiantes (models.Model):
    nombre = models.CharField (max_length = 50, blank = True, null = True)
    apellido = models.CharField (max_length = 50, blank = True, null = True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Profesores (models.Model):
    nombre = models.CharField (max_length = 50, blank = True, null = True)
    apellido = models.CharField (max_length = 50, blank = True, null = True)
    materia = models.CharField (max_length = 50, blank = True, null = True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Materias (models.Model):
    nombreMateria = models.CharField (max_length = 50, blank = True, null = True)
    nivel = models.CharField (max_length = 50, blank = True, null = True)

    def __str__(self):
        return self.nombreMateria
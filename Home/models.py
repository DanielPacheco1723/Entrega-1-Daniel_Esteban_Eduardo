from __future__ import unicode_literals
from django.db import models

class Estudiantes (models.Model):
    nombre = models.CharField (max_length = 50, blank = True, null = True)
    apellido = models.CharField (max_length = 50, blank = True, null = True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
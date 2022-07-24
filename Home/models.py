from __future__ import unicode_literals
from django.db import models

class Registrado (models.Model):
    nombre = models.CharField (max_length = 50, blank = True, null = True)
    email = models.EmailField()
    timestamp = models.DateTimeField (auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.email
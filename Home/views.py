from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiantes

def index (request):
    estudiantes = Estudiantes.objects.all()
    return render (request, "index.html", {"Estudiante": estudiantes})





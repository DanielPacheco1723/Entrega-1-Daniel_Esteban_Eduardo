from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiantes, Profesores, Materias

def index (request):
    estudiantes = Estudiantes.objects.all()
    return render (request, "inicio.html", {"Estudiante": estudiantes})

def profesores (request):
    profesores = Profesores.objects.all()
    return render (request, "profesores.html", {"Profesor": profesores})

def materias (request):
    materias = Materias.objects.all()
    return render (request, "materias.html", {"Materia": materias})





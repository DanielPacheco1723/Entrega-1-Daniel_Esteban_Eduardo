from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiantes, Profesores, Materias
from django.db.models import Q

def index (request):
    estudiantes = Estudiantes.objects.all()
    return render (request, "inicio.html", {"Estudiante": estudiantes})

def profesores (request):
    profesores = Profesores.objects.all()
    busdb= request.GET.get("buscarDB")
    if busdb:
        profesorbuscado = Profesores.objects.filter(Q(nombre__icontains = busdb)|Q(apellido__icontains = busdb)|Q(materia__icontains = busdb)|Q(email__icontains = busdb)).distinct()
        return render(request, "profesores.html", {"Profesor": profesores,"profesorbuscado": profesorbuscado})
    return render (request, "profesores.html", {"Profesor": profesores})

def materias (request):
    materias = Materias.objects.all()
    return render (request, "materias.html", {"Materia": materias})

def busqueda(request):
    busdb= request.GET.get("buscarDB")
    estudiantes = Estudiantes.objects.all()
    if busdb:
        print(busdb)
        estudiante = Estudiantes.objects.filter(Q(nombre__icontains = busdb)).distinct()
        return render(request, "busqueda.html", {"Estudiante": estudiante})
    return render (request, "inicio.html", {"Estudiante": estudiantes})



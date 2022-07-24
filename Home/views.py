from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiante

def index (request):
    
    estudiantes = Estudiante.objects.all()

    return render (request, "Home/index.html",{"estudiantes": estudiantes})




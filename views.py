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

def EstudianteFormulario(request):
    print('method:', request.method)
    print('post', request.POST)
    
    if request.method == "POST":
        Estudiante = Estudiantes(nombre=request.POST['Nombre'], apellido=request.POST['Apellido'], email=request.POST['Email'])
        Estudiante.save()
        return render(request,"inicio.html")
    return render(request, "estudianteForm.html")

def PorfesorFormulario(request):
    print('method:', request.method)
    print('post', request.POST)
    
    if request.method == "POST":
        Profesor = Profesores(nombre=request.POST['Nombre'], apellido=request.POST['Apellido'],materia=request.POST['Materia'], email=request.POST['Email'])
        Profesor.save()
        return render(request,"ProfesorForm.html")
    return render(request, "ProfesorForm.html")

def MateriaFormulario(request):
    print('method:', request.method)
    print('post', request.POST)
    
    if request.method == "POST":
        Materia = Materias(nombreMateria=request.POST['NombreMateria'], nivel=request.POST['Nivel'])
        Materia.save()
        return render(request,"inicio.html")
    return render(request, "materiaForm.html")    

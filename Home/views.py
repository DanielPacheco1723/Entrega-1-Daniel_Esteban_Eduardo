from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Estudiantes, Profesores, Materias

def index (request):
    busdb= request.GET.get("buscarDB")
    estudiantes = Estudiantes.objects.all()
    if busdb:
        print(busdb)
        estudiantebuscado = Estudiantes.objects.filter(Q(nombre__icontains = busdb)|Q(apellido__icontains = busdb)|Q(email__icontains = busdb)).distinct()
        return render(request, "busqueda.html", {"Estudiante": estudiantes,"estudiantebuscado":estudiantebuscado})
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

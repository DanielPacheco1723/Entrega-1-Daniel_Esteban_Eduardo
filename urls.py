from django.urls import path
from .views import *

urlpatterns = [
    path ('', index, name = "inicio"),
    path ('Profesores/', profesores, name = "profesores"),
    path ('Materias/', materias,name = "materias"),
    path ('estudianteForm/', EstudianteFormulario, name="EstudianteFormulario") ,
    path ('profesorForm/', PorfesorFormulario, name="ProfesorFormulario") ,
]
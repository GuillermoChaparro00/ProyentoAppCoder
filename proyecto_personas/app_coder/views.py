import re
from unittest import loader
import django
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Personas , Profesores , Curso
 
from django.template import loader
from app_coder.forms import Alumnos_formulario,  Curso_formulario , UserEditForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required


def plantilla(request):
    return render(request, "plantilla.html")

def about(request):
    return render(request, "about.html")





##ALUMNOOS
def alumnos(request):
    los_alumnos=Personas.objects.all()
    diccionario={"alumnos": los_alumnos}
    platilla=loader.get_template("alumnos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)

@login_required
def cargar_alumno(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            persona= Personas(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            persona.save()

            los_alumnos=Personas.objects.all()

            return render(request, "alumnos.html", {"alumnos":los_alumnos})
    return render(request, "cargar_alumno.html")




def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"] 
        alumnos=Personas.objects.filter(nombre__icontains =nombre)
        return render(request,"alumnos.html",{"alumnos":alumnos})
    else:
        return HttpResponse("campo vacio")

@login_required
def eliminar_alumno(request,id):
    alumno=Personas.objects.get(id=id)
    alumno.delete()

    alumno=Personas.objects.all()
    return render(request,"alumnos.html",{"alumnos":alumno})

@login_required
def editar_alumno(request,id):
    alumno=Personas.objects.get(id=id)

    if request.method =="POST":
        mi_formulario=Alumnos_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumno.nombre=datos['nombre']
            alumno.apellido=datos['apellido']
            alumno.edad=datos['edad']
            alumno.edad=datos['dni']
            alumno.nacimiento=datos['nacimiento']
            alumno.save()
            alumnos=Personas.objects.all()
            return render(request,"alumnos.html",{"alumnos":alumnos})
    else:
        mi_formulario=Curso_formulario(initial={'nombre':alumno.nombre,'apellido':alumno.apellido,'edad':alumno.edad,'dni':alumno.dni,'nacimiento':alumno.nacimiento})
    return render(request, "editar_alumno.html",{"mi_formulario":mi_formulario,"alumno":alumno})  
    
##fin alumnos




#-----------------------------

##PROFESORES 

def profesores(request):
    los_profes=Profesores.objects.all()
    diccionario={"profesores": los_profes}
    platilla=loader.get_template("profesores.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento) 


@login_required
def cargar_profesores(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            Profe= Profesores(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            Profe.save()
            los_profesores=Profesores.objects.all()
            return render(request, "profesores.html", {"profesores":los_profesores})

    return render(request, "cargar_profesores.html")


@login_required
def eliminar_profesor(request,id):
    profesor=Profesores.objects.get(id=id)
    profesor.delete()

    profesor=Profesores.objects.all()
    return render(request,"profesores.html",{"profesores":profesor})


def buscar_profesor(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"] 
        nombres=Profesores.objects.filter(nombre__icontains =nombre)
        return render(request,"profesores.html",{"profesores":nombres})
    else:
        return HttpResponse("campo vacio")

@login_required
def editar_profesor(request,id):
    profesor=Profesores.objects.get(id=id)

    if request.method =="POST":
        mi_formulario=Alumnos_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesor.nombre=datos['nombre']
            profesor.apellido=datos['apellido']
            profesor.edad=datos['edad']
            profesor.edad=datos['dni']
            profesor.nacimiento=datos['nacimiento']
            profesor.save()
            profesores=Profesores.objects.all()
            return render(request,"profesores.html",{"profesores":profesores})
    else:
        mi_formulario=Curso_formulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'edad':profesor.edad,'dni':profesor.dni,'nacimiento':profesor.nacimiento})
    return render(request, "editar_profesor.html",{"mi_formulario":mi_formulario,"profesor":profesor})  

    

##FIN PROFESORES


#-------------------------------------



##CURSOS

def cursos(request):
    los_cursos=Curso.objects.all()
    diccionario={"cursos": los_cursos}
    platilla=loader.get_template("cursos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)  

@login_required
def cargar_curso(request):
    if request.method=="POST":
        validacionForm= Curso_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            cursos= Curso(nombre= datos["nombre"],camada=datos["camada"],turno=datos["turno"])
            cursos.save()
            los_cursos=Curso.objects.all()

            return render(request, "cursos.html", {"cursos":los_cursos})            
    return render(request, "cargar_curso.html")


@login_required
def eliminar_curso(request,id):
    curso=Curso.objects.get(id=id)
    curso.delete()

    cursos=Curso.objects.all()
    return render(request,"cursos.html",{"cursos":cursos})


def buscar_curso(request):
    if request.GET["curso"]:
        curso=request.GET["curso"] 
        cursos=Curso.objects.filter(nombre__icontains =curso)
        return render(request,"cursos.html",{"cursos":cursos})
    else:
        return HttpResponse("campo vacio")

@login_required
def editar_curso(request,id):
    curso=Curso.objects.get(id=id)

    if request.method =="POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso.nombre=datos['nombre']
            curso.camada=datos['camada']
            curso.turno=datos['turno']
            curso.save()
            cursos=Curso.objects.all()
            return render(request,"cursos.html",{"cursos":cursos})
    else:
        mi_formulario=Curso_formulario(initial={'nombre':curso.nombre,'camada':curso.camada,'turno':curso.turno})
    return render(request, "editar_curso.html",{"mi_formulario":mi_formulario,"curso":curso})    
##FIN CURSOS



##INICIO LOGIN

def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user=authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                return render(request,"inicio.html", {"nombreUsuario":usuario})
            else:
                return HttpResponse("usuario incorrecto")
        else:
            return HttpResponse(f"Form incorrecto {form}")

    form=  AuthenticationForm()
    return render (request, "login.html", {"form":form})

##FIN LOGIN


##inicio registro

def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,"inicio.html")


    else:
        form=UserCreationForm()
    return render(request, "registro.html", {"form":form})

##fin registro

##editar perfil
@login_required
def EditarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion=miFormulario.cleaned_data
            usuario.email= informacion["email"]
            password=informacion["password1"]
            usuario.set_password(password)
            usuario.save()
        

    else:
        miFormulario= UserEditForm(initial={'email':usuario.email})
    return render(request,"editar_perfil.html" ,{'miFormulario':miFormulario,'usuario':usuario})



##fin editar perfil

##perfil
@login_required
def perfil(request):
    return render(request, "inicio.html")
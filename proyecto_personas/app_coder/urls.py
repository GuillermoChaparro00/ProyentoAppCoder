from re import template
from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns=[

   
    path("",views.plantilla, name="index"),
    path("buscar",views.buscar, name="buscar"),
    path("about",views.about, name="about"),


    #alumnos
    path("alumnos",views.alumnos, name="alumnos"),
    path("cargar_alumno",views.cargar_alumno, name="cargar_alumno"),
    path("eliminar_alumno/<int:id>",views.eliminar_alumno, name="eliminar_alumno"),

    path("editar_alumno/<int:id>",views.editar_alumno, name="editar_alumno"),
    path("editar_alumno/",views.editar_alumno, name="editar_alumno"),



    #cursos
    path("cursos",views.cursos, name="cursos"),
    path("cargar_curso",views.cargar_curso, name="cargar_curso"),
    path("eliminar_curso/<int:id>",views.eliminar_curso, name="eliminar_curso"),
    path("buscar_curso",views.buscar_curso, name="buscar_curso"),

    path("editar_curso/<int:id>",views.editar_curso, name="editar_curso"),
    path("editar_curso",views.editar_curso, name="editar_curso"),



    #profesores
    path("profesores",views.profesores, name="profesores"),
    path("cargar_profesores",views.cargar_profesores, name="cargar_profesores"),
    path("eliminar_profesor/<int:id>",views.eliminar_profesor, name="eliminar_profesor"),
    path("buscar_profesor",views.buscar_profesor, name="buscar_profesor"),

    path("editar_profesor/<int:id>",views.editar_profesor, name="editar_profesor"),
    path("editar_profesor/",views.editar_profesor, name="editar_profesor"),



    #perfil
    path("perfil",views.perfil, name="perfil"),
    #login
    path("login",views.login_request, name="login"),

    #registro
    path("register",views.register, name="register"),

    #logaut
     path("logout",LogoutView.as_view(template_name="plantilla.html"), name="logout"),

    #editar perfil
     path("EditarPerfil",views.EditarPerfil, name="EditarPerfil"),





]
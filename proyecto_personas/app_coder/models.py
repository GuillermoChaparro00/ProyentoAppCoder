from distutils.command.upload import upload
from pyexpat import model
from urllib import request
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Personas(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    dni=models.IntegerField()
    nacimiento=models.DateField()

class Profesores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    dni=models.IntegerField()
    nacimiento=models.DateField()

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    turno=models.CharField(max_length=15)


#class Avatar(models.Model):
#    User=models.ForeignKey(User, on_delete=models.CASCADE)
#    imagen=models.ImageField(upload_to="avatares",null=True, blank=True)

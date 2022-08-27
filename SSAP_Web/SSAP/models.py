from django.db import models
from django.contrib.auth.models import User

# Modelos

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key = True)
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key= True)
    nombre_empresa = models.CharField(max_length=200, null= False)
    rubro_empresa = models.CharField(max_length=200, null= False)
    cant_trabajadores = models.IntegerField(null= False)

class Administradores(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key= True)
    nombre = models.CharField(max_length=200, null= False)
    
class Profesionales(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key= True)
    nombre = models.CharField(max_length=200, null= False)
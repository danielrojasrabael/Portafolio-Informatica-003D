from django.db import models
from django.contrib.auth.models import User

# Modelos

class Usuario(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key= True)
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    class Meta:
        db_table = "usuario"
    def __str__(self):
        return u'{0}'.format(self.rut)

class Cliente(Usuario):
    nombre_empresa = models.CharField(max_length=200, null= False)
    rubro_empresa = models.CharField(max_length=200, null= False)
    cant_trabajadores = models.IntegerField(null= False)

    class Meta:
        db_table = "cliente"

class Administrador(Usuario):
    nombre = models.CharField(max_length=200, null= False)

    class Meta:
        db_table = "administrador"
    
class Profesional(Usuario):
    nombre = models.CharField(max_length=200, null= False)

    class Meta:
        db_table = "profesional"
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Modelos

class Usuario(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key= True)
    tipo = models.CharField(max_length=20, null= False)
    direccion = models.CharField(max_length=200, null= False)
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

class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    costo_base = models.IntegerField(null=False)
    fecha_firma = models.DateField(null=False)
    ultimo_pago = models.DateField(null=False)
    CLIENTE_rut = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    PROFESIONAL_rut = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    class Meta:
        db_table = "contrato"

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, null=False)
    descripcion = models.TextField(null=False)
    fecha = models.DateField(null=False)
    CLIENTE_rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    class Meta:
        db_table = "notificacion"

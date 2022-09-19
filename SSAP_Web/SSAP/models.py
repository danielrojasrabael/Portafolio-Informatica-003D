# Imports

from http import client
from django.db import models
import cx_Oracle

# Variables

conn = cx_Oracle.connect(user="SSAP", password="123456", dsn="localhost:1521/XE")
conn.autocommit = True

# Modelos
#   Gestión de Usuario
class Usuario(models.Model):
    id_usuario = models.IntegerField()
    contraseña = models.CharField(max_length=999)
    tipo = models.CharField(max_length=999)
    id_comuna = models.CharField(max_length=999)
    direccion = models.CharField(max_length=999)
    estado = models.IntegerField()
    def guardar(self):
        cur = conn.cursor()
        cur.callproc("INSERTARUSUARIO", [self.contraseña, self.tipo, self.id_comuna, self.direccion])
        cur.close()
    def todos(orden_id=False):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARUSUARIOS", [datos, orden_id])
        lista = []
        for i in datos:
            usuario = Usuario(id_usuario=i[0],contraseña=i[1],tipo=i[2],id_comuna=i[3],direccion=i[4], estado=i[5])
            lista.append(usuario)
        cur.close()
        datos.close()
        return lista
    def filtro_id(id=None):
        cur = conn.cursor()
        datos = conn.cursor()
        usuario = None
        cur.callproc("USUARIO_PORID", [datos, id])
        for i in datos:
            usuario = Usuario(id_usuario=i[0],contraseña=i[1],tipo=i[2],id_comuna=i[3],direccion=i[4], estado=i[5])
        cur.close()
        datos.close()
        return usuario
    def deshabilitar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARUSUARIO", [self.id_usuario,self.contraseña, self.tipo, self.id_comuna, self.direccion, 0])
        cur.close()
    def habilitar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARUSUARIO", [self.id_usuario,self.contraseña, self.tipo, self.id_comuna, self.direccion, 1])
        cur.close()
    def actualizar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARUSUARIO", [self.id_usuario,self.contraseña, self.tipo, self.id_comuna, self.direccion, self.estado])
        cur.close()
    class Meta:
        managed = False

class Cliente(models.Model):
    id_usuario = models.IntegerField()
    rut = models.CharField(max_length=999)
    nombre_empresa = models.CharField(max_length=999)
    rubro_empresa = models.CharField(max_length=999)
    cant_trabajadores = models.IntegerField()
    def guardar(self):
        cur = conn.cursor()
        cur.callproc("INSERTARCLIENTE", [self.id_usuario, self.rut, self.nombre_empresa, self.rubro_empresa, self.cant_trabajadores])
        cur.close()
    def todos():
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARCLIENTES", [datos])
        lista = []
        for i in datos:
            cliente = Cliente(id_usuario=i[0],rut=i[1],nombre_empresa=i[2],rubro_empresa=i[3],cant_trabajadores=i[4])
            lista.append(cliente)
        cur.close()
        datos.close()
        return lista
    def filtro_rut(rut=None):
        cur = conn.cursor()
        datos = conn.cursor()
        cliente = None
        cur.callproc("CLIENTE_PORRUT", [datos,rut])
        for i in datos:
            cliente = Cliente(id_usuario=i[0],rut=i[1],nombre_empresa=i[2],rubro_empresa=i[3],cant_trabajadores=i[4])
        cur.close()
        datos.close()
        return cliente
    def filtro_id(id=None):
        cur = conn.cursor()
        datos = conn.cursor()
        cliente = None
        cur.callproc("CLIENTE_PORID", [datos,id])
        for i in datos:
            cliente = Cliente(id_usuario=i[0],rut=i[1],nombre_empresa=i[2],rubro_empresa=i[3],cant_trabajadores=i[4])
        cur.close()
        datos.close()
        return cliente
    def actualizar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARCLIENTE", [self.id_usuario, self.rut, self.nombre_empresa, self.rubro_empresa, self.cant_trabajadores])
        cur.close()
    class Meta:
        managed = False

class Administrador(models.Model):
    id_usuario = models.IntegerField()
    rut = models.CharField(max_length=999)
    nombre = models.CharField(max_length=999)
    def guardar(self):
        cur = conn.cursor()
        cur.callproc("INSERTARADMINISTRADOR", [self.id_usuario,self.rut,self.nombre])
        cur.close()
    def todos():
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARADMINISTRADORES", [datos])
        lista = []
        for i in datos:
            administrador = Administrador(id_usuario=i[0],rut=i[1],nombre=i[2])
            lista.append(administrador)
        cur.close()
        datos.close()
        return lista
    def filtro_rut(rut=None):
        cur = conn.cursor()
        datos = conn.cursor()
        administrador = None
        cur.callproc("ADMIN_PORRUT", [datos,rut])
        for i in datos:
            administrador = Administrador(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return administrador
    def filtro_id(id=None):
        cur = conn.cursor()
        datos = conn.cursor()
        administrador = None
        cur.callproc("ADMIN_PORID", [datos,id])
        for i in datos:
            administrador = Administrador(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return administrador
    def actualizar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARADMINISTRADOR", [self.id_usuario, self.rut, self.nombre])
        cur.close()
    class Meta:
        managed = False
    
class Profesional(models.Model):
    id_usuario = models.IntegerField()
    rut = models.CharField(max_length=999)
    nombre = models.CharField(max_length=999)
    def guardar(self):
        cur = conn.cursor()
        cur.callproc("INSERTARPROFESIONAL", [self.id_usuario,self.rut,self.nombre])
        cur.close()
    def todos():
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARPROFESIONALES", [datos])
        lista = []
        for i in datos:
            profesional = Profesional(id_usuario=i[0],rut=i[1],nombre=i[2])
            lista.append(profesional)
        cur.close()
        datos.close()
        return lista
    def filtro_rut(rut=None):
        cur = conn.cursor()
        datos = conn.cursor()
        profesional = None
        cur.callproc("PROFESIONAL_PORRUT", [datos,rut])
        for i in datos:
            profesional = Profesional(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return profesional
    def filtro_id(id=None):
        cur = conn.cursor()
        datos = conn.cursor()
        profesional = None
        cur.callproc("PROFESIONAL_PORID", [datos,id])
        for i in datos:
            profesional = Profesional(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return profesional
    def actualizar(self):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARPROFESIONAL", [self.id_usuario, self.rut, self.nombre])
        cur.close()
    class Meta:
        managed = False

#   Funciones de Cliente

class Contrato(models.Model):
    id_contrato = models.IntegerField()
    costo_base = models.IntegerField()
    fecha_firma = models.DateField()
    ultimo_pago = models.DateField()
    CLIENTE_rut = models.CharField(max_length=999)
    PROFESIONAL_rut = models.CharField(max_length=999)
    def guardar(self):
        cur = conn.cursor()
        cur.callproc("INSERTARCONTRATO", [self.costo_base, self.fecha_firma, self.CLIENTE_rut, self.PROFESIONAL_rut])
        cur.close()
    class Meta:
        managed = False

class Notificacion(models.Model):
    id_notificacion = models.IntegerField()
    titulo = models.CharField(max_length=999)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    CLIENTE_rut = models.CharField(max_length=999)
    def todos(rut=None):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARNOTIFICACIONES", [datos,rut])
        lista = []
        for i in datos:
            notificacion = Notificacion(id_notificacion=i[0],titulo=i[1],descripcion=i[2],fecha=i[3],CLIENTE_rut=i[4])
            lista.append(notificacion)
        cur.close()
        datos.close()
        return lista
    def eliminar(id=None, rut=None):
        cur = conn.cursor()
        cur.callproc("ELIMINARNOTIFICACION", [id,rut])
        cur.close()
    class Meta:
        managed = False

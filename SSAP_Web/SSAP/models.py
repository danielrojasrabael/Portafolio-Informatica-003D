# Imports

from django.db import models
from datetime import date
import cx_Oracle

# Variables

conexion = cx_Oracle.connect(user="SSAP", password="123456", dsn="localhost:1522/ORCL1")
conexion.autocommit = True

# Modelos
#   Gestión de Usuario
class Usuario(models.Model):
    id_usuario = models.IntegerField()
    contraseña = models.CharField(max_length=999)
    tipo = models.CharField(max_length=999)
    id_comuna = models.CharField(max_length=999)
    direccion = models.CharField(max_length=999)
    estado = models.IntegerField()
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARUSUARIO", [self.contraseña, self.tipo, self.id_comuna, self.direccion])
        cur.close()
    def todos(orden_id=False, conn=conexion):
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
    def filtro_id(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        usuario = None
        cur.callproc("USUARIO_PORID", [datos, id])
        for i in datos:
            usuario = Usuario(id_usuario=i[0],contraseña=i[1],tipo=i[2],id_comuna=i[3],direccion=i[4], estado=i[5])
        cur.close()
        datos.close()
        return usuario
    def deshabilitar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARUSUARIO", [self.id_usuario,self.contraseña, self.tipo, self.id_comuna, self.direccion, 0])
        cur.close()
    def habilitar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARUSUARIO", [self.id_usuario,self.contraseña, self.tipo, self.id_comuna, self.direccion, 1])
        cur.close()
    def actualizar(self, conn=conexion):
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
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARCLIENTE", [self.id_usuario, self.rut, self.nombre_empresa, self.rubro_empresa, self.cant_trabajadores])
        cur.close()
    def todos(conn=conexion):
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
    def filtro_rut(rut=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cliente = None
        cur.callproc("CLIENTE_PORRUT", [datos,rut])
        for i in datos:
            cliente = Cliente(id_usuario=i[0],rut=i[1],nombre_empresa=i[2],rubro_empresa=i[3],cant_trabajadores=i[4])
        cur.close()
        datos.close()
        return cliente
    def filtro_id(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cliente = None
        cur.callproc("CLIENTE_PORID", [datos,id])
        for i in datos:
            cliente = Cliente(id_usuario=i[0],rut=i[1],nombre_empresa=i[2],rubro_empresa=i[3],cant_trabajadores=i[4])
        cur.close()
        datos.close()
        return cliente
    def actualizar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARCLIENTE", [self.id_usuario, self.rut, self.nombre_empresa, self.rubro_empresa, self.cant_trabajadores])
        cur.close()
    class Meta:
        managed = False

class Administrador(models.Model):
    id_usuario = models.IntegerField()
    rut = models.CharField(max_length=999)
    nombre = models.CharField(max_length=999)
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARADMINISTRADOR", [self.id_usuario,self.rut,self.nombre])
        cur.close()
    def todos(conn=conexion):
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
    def filtro_rut(rut=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        administrador = None
        cur.callproc("ADMIN_PORRUT", [datos,rut])
        for i in datos:
            administrador = Administrador(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return administrador
    def filtro_id(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        administrador = None
        cur.callproc("ADMIN_PORID", [datos,id])
        for i in datos:
            administrador = Administrador(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return administrador
    def actualizar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARADMINISTRADOR", [self.id_usuario, self.rut, self.nombre])
        cur.close()
    class Meta:
        managed = False
    
class Profesional(models.Model):
    id_usuario = models.IntegerField()
    rut = models.CharField(max_length=999)
    nombre = models.CharField(max_length=999)
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARPROFESIONAL", [self.id_usuario,self.rut,self.nombre])
        cur.close()
    def todos(conn=conexion):
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
    def filtro_rut(rut=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        profesional = None
        cur.callproc("PROFESIONAL_PORRUT", [datos,rut])
        for i in datos:
            profesional = Profesional(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return profesional
    def filtro_id(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        profesional = None
        cur.callproc("PROFESIONAL_PORID", [datos,id])
        for i in datos:
            profesional = Profesional(id_usuario=i[0],rut=i[1],nombre=i[2])
        cur.close()
        datos.close()
        return profesional
    def actualizar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARPROFESIONAL", [self.id_usuario, self.rut, self.nombre])
        cur.close()
    class Meta:
        managed = False

class Ubicacion(models.Model):
    id_comuna = models.IntegerField()
    nombre_comuna = models.CharField(max_length=999)
    nombre_ciudad = models.CharField(max_length=999)
    nombre_region = models.CharField(max_length=999)
    def todos(conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARUBICACION", [datos])
        lista = []
        for i in datos:
            ubicacion = Ubicacion(id_comuna=i[0],nombre_comuna=i[1],nombre_ciudad=i[2],nombre_region=i[3])
            lista.append(ubicacion)
        cur.close()
        datos.close()
        return lista
    class Meta:
        managed = False

# Funciones Profesional Cliente

class Contrato(models.Model):
    id_contrato = models.IntegerField()
    costo_base = models.IntegerField()
    fecha_firma = models.DateField()
    ultimo_pago = models.DateField()
    CLIENTE_rut = models.CharField(max_length=999)
    PROFESIONAL_rut = models.CharField(max_length=999)
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARCONTRATO", [self.costo_base, self.fecha_firma, self.CLIENTE_rut, self.PROFESIONAL_rut])
        cur.close()
    def filtro_rutcliente(rut=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        contrato = None
        cur.callproc("CONTRATO_PORRUTCLIENTE", [datos,rut])
        for i in datos:
            contrato = Contrato(id_contrato=i[0], costo_base=i[1],fecha_firma=i[2],ultimo_pago=i[3],CLIENTE_rut=i[4],PROFESIONAL_rut=i[5])
        cur.close()
        datos.close()
        return contrato
    def seleccionar_rutprofesional(rut=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        contratos = []
        cur.callproc("CONTRATOS_PORRUTPROFESIONAL", [datos,rut])
        for i in datos:
            contrato = Contrato(id_contrato=i[0], costo_base=i[1],fecha_firma=i[2],ultimo_pago=i[3],CLIENTE_rut=i[4],PROFESIONAL_rut=i[5])
            contratos.append(contrato)
        cur.close()
        datos.close()
        return contratos
    class Meta:
        managed = False

class Checklist(models.Model):
    id_checklist = models.IntegerField()
    elementos = models.TextField()
    id_contrato = models.IntegerField()
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARCHECKLIST", [self.id_contrato])
        cur.close()
    def actualizar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARCHECKLIST", [self.elementos,self.id_contrato])
        cur.close()
    def filtro_idcontrato(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        checklist = None
        cur.callproc("CHECKLIST_PORIDCONTRATO", [datos,id])
        for i in datos:
            checklist = Checklist(id_checklist=i[0],elementos=i[1],id_contrato=i[2])
        cur.close()
        datos.close()
        return checklist
    class Meta:
        managed = False

#   Funciones de Cliente

class Mensualidad(models.Model):
    id_mensualidad = models.IntegerField()
    fecha_limite = models.DateField()
    estado = models.IntegerField()
    costo = models.IntegerField()
    id_contrato = models.IntegerField()
    fecha_pago = models.DateField()
    boleta = models.CharField(max_length=999)
    def todos_idcontrato(id,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        lista = []
        cur.callproc("PAGO_PORIDCONTRATO", [datos,id])
        for i in datos:
            mensualidad = Mensualidad(id_mensualidad=i[0],fecha_limite=i[1],estado=i[2],costo=i[3],id_contrato=i[4], fecha_pago=i[5], boleta=i[6])
            lista.append(mensualidad)
        cur.close()
        datos.close()
        return lista
    def esta_atrasado(self):
        return date.today() > self.fecha_limite.date()
    class Meta:
        managed = False


class Notificacion(models.Model):
    id_notificacion = models.IntegerField()
    titulo = models.CharField(max_length=999)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    CLIENTE_rut = models.CharField(max_length=999)
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARNOTIFICACION", [self.titulo,self.descripcion,self.fecha,self.CLIENTE_rut])
        cur.close()
    def todos(rut=None, conn=conexion):
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
    def eliminar(id=None, rut=None, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ELIMINARNOTIFICACION", [id,rut])
        cur.close()
    class Meta:
        managed = False

#   Funciones Profesionales

class Visita(models.Model):
    id_visita = models.IntegerField()
    fecha = models.DateField()
    estado = models.IntegerField()
    ubicacion = models.CharField(max_length=999)
    reporte_final = models.CharField(max_length=999)
    periodo = models.DateField()
    CONTRATO_id = models.IntegerField()
    COMUNA_id_comuna = models.IntegerField()
    nombre_cliente = models.CharField(max_length=999)
    def filtro_id(id=None, conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        visita = None
        cur.callproc("VISITA_PORID", [datos,id])
        for i in datos:
            visita = Visita(id_visita=i[0], fecha=i[1], estado=i[2],ubicacion=i[3], reporte_final = i[4], periodo=i[5], CONTRATO_id=i[6],COMUNA_id_comuna=i[7], nombre_cliente=i[8])
        cur.close()
        datos.close()
        return visita
    def modificar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARVISITA", [self.fecha,self.estado,self.ubicacion,self.reporte_final,self.periodo,self.COMUNA_id_comuna,self.id_visita])
        cur.close()
    def todos(conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SELECCIONARVISITAS", [datos])
        lista = []
        for i in datos:
            visita = Visita(id_visita=i[0], fecha=i[1], estado=i[2],ubicacion=i[3], reporte_final = i[4], periodo=i[5], CONTRATO_id=i[6],COMUNA_id_comuna=i[7], nombre_cliente=i[8])
            lista.append(visita)
        cur.close()
        datos.close()
        return lista
    class Meta:
        managed = False

# Funciones de Administrador

class Actividad(models.Model):
    nombre_profesional = models.CharField(max_length=999)
    tipo = models.CharField(max_length=999)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=999)
    def obtener(rut=None, conn=conexion):
        #Visita
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("ACTIVIDADPROFVISITA", [datos,rut])
        lista = []
        for i in datos:
            actividad = Actividad(nombre_profesional=i[3],tipo="Visita",fecha=i[0],ubicacion=i[1]+", "+i[2])
            lista.append(actividad)
        
        #Capacitacion
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("ACTIVIDADPROFCAPACITACION", [datos,rut])
        for i in datos:
            actividad = Actividad(nombre_profesional=i[4],tipo="Capacitacion",fecha=i[1],ubicacion=i[2]+", "+i[3])
            lista.append(actividad)

        #Asesoria
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("ACTIVIDADPROFASESORIA", [datos,rut])
        for i in datos:
            actividad = Actividad(nombre_profesional=i[2],tipo="Asesoria",fecha=i[1],ubicacion="N/A")
            lista.append(actividad)
        cur.close()
        datos.close()
        return lista
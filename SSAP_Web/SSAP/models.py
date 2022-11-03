# Imports

from unittest.util import _MAX_LENGTH
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
    NOMBRE_contrato = models.CharField(max_length=999)

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
    def filtro_id(id,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("PAGO_PORIDMENSUALIDAD", [datos,id])
        for i in datos:
            mensualidad = Mensualidad(id_mensualidad=i[0],fecha_limite=i[1],estado=i[2],costo=i[3],id_contrato=i[4], fecha_pago=i[5], boleta=i[6])
        cur.close()
        datos.close()
        return mensualidad
    def actualizar(self,conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARMENSUALIDAD", [self.estado,self.fecha_pago,self.boleta,self.id_mensualidad])
        cur.close()
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

class Solicitud(models.Model):
    id_solicitud = models.IntegerField()
    estado = models.CharField(max_length=999)
    tipo = models.CharField(max_length=999)
    fecha_publicacion = models.DateTimeField()
    motivo = models.TextField()
    archivo = models.CharField(max_length=999)
    CONTRATO_id_contrato = models.IntegerField()
    nombre_cliente = models.CharField(max_length=999)
    def todos_idcontrato(id,conn=conexion):
        cur = conn.cursor()
        datosAs = conn.cursor()
        datosCap = conn.cursor()
        lista = []
        cur.callproc("SOLICITUD_PORIDCONTRATO", [datosAs,datosCap,id])
        for i in datosAs:
            solicitud = Solicitud(motivo=i[0],tipo=i[1],fecha_publicacion=i[2],estado=i[3],id_solicitud=i[4], archivo=i[5], nombre_cliente=i[6])
            lista.append(solicitud)
        for i in datosCap:
            solicitud = Solicitud(motivo=i[0],tipo=i[1],fecha_publicacion=i[2],estado=i[3],id_solicitud=i[4], archivo=i[5], nombre_cliente=i[6])
            lista.append(solicitud)
        cur.close()
        datosAs.close()
        datosCap.close()
        return lista
    class Meta:
        managed = False
    
class Asesoria(Solicitud):
    id_asesoria = models.IntegerField()
    tipo_asesoria = models.CharField(max_length=999)
    respuesta = models.TextField()
    fecha_respuesta = models.DateTimeField()
    def guardar(self,conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARASESORIA", [self.tipo,self.CONTRATO_id_contrato,self.fecha_publicacion,self.motivo,self.archivo,self.tipo_asesoria])
        cur.close()
    def filtro_idsolicitud(id=None,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("ASESORIA_PORIDSOLICITUD", [datos,id])
        for i in datos:
            asesoria = Asesoria(motivo = i[0],tipo = i[1], fecha_publicacion = i[2], estado = i[3], id_solicitud=i[4], respuesta = i[5], fecha_respuesta = i[6], archivo = i[7])
        cur.close()
        datos.close()
        return asesoria
    class Meta:
        managed = False

class SolicitudCapacitacion(Solicitud):
    def guardar(self,conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARSOLICITUDCAPACITACION", [self.tipo,self.CONTRATO_id_contrato,self.fecha_publicacion,self.motivo,self.archivo])
        cur.close()
    def filtro_idsolicitud(id=None,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("SOLICITUD_CAPACITACION_PORIDSOLICITUD", [datos,id])
        for i in datos:
            solicitudcapacitacion = SolicitudCapacitacion(motivo = i[0],tipo = i[1], fecha_publicacion = i[2], estado = i[3], id_solicitud=i[4], archivo = i[5])
        cur.close()
        datos.close()
        return solicitudcapacitacion
    class Meta:
        managed = False

class Capacitacion(models.Model):
    id_capacitacion = models.IntegerField()
    nombre = models.CharField(max_length=999)
    ubicacion = models.CharField(max_length=999)
    estado = models.CharField(max_length=999)
    duracion = models.IntegerField()
    fecha = models.DateField()
    CONTRATO_id_contrato = models.IntegerField()
    COMUNA_id_comuna = models.IntegerField()
    nombre_cliente = models.CharField(max_length=999)
    def filtro_idcontrato(id=None,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        capacitaciones = []
        cur.callproc("CAPACITACION_PORIDCONTRATO", [datos,id])
        for i in datos:
            capacitacion = Capacitacion(id_capacitacion = i[0], nombre = i[1], ubicacion = i[2], estado = i[3], fecha = i[4],CONTRATO_id_contrato = i[5], duracion = i[6], nombre_cliente=i[7])
            capacitaciones.append(capacitacion)
        cur.close()
        datos.close()
        return capacitaciones
    def filtro_id(id=None,conn=conexion):
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("CAPACITACION_PORID", [datos,id])
        for i in datos:
            capacitacion = Capacitacion(id_capacitacion =  i[0],nombre = i[1],ubicacion = i[2],estado = i[3],duracion = i[4],fecha = i[5],CONTRATO_id_contrato = i[6],COMUNA_id_comuna = i[7], nombre_cliente=i[8])
        cur.close()
        datos.close()
        return capacitacion
    def actualizar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("ACTUALIZARCAPACITACION", [self.estado,self.id_capacitacion])
        cur.close()
    def guardar(self, conn=conexion):
        cur = conn.cursor()
        cur.callproc("INSERTARCAPACITACION", [self.nombre,self.ubicacion,self.fecha,self.CONTRATO_id_contrato,self.COMUNA_id_comuna,self.duracion])
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
    class Meta:
        managed = False

# Modelos Especializados

class Pago_Mensual(models.Model):
    año = models.IntegerField()
    mes = models.CharField(max_length=999)
    costo = models.IntegerField()
    def todos(conn=conexion):
        idiomas = {"January":"Enero","February":"Febrero","March":"Marzo","April":"Abril","May":"Mayo","June":"Junio","July":"Julio","August":"Agosto","September":"Septiembre","October":"Octubre","November":"Noviembre","December":"Diciembre"}
        cur = conn.cursor()
        datos = conn.cursor()
        cur.callproc("PA_BUSCAR_PAGOS", [datos])
        lista = []
        for i in datos:
            m = str(i[1]).strip()
            pago_mensual = Pago_Mensual(año = i[0], mes=idiomas[m], costo = i[2])
            lista.append(pago_mensual)
        cur.close()
        datos.close()
        return lista
    class Meta:
        managed = False
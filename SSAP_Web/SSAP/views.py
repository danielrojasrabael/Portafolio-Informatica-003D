#Imports
import mimetypes
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime
from xmlrpc.client import DateTime
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
import calendar
from django.core.mail import send_mail
from django.utils.html import strip_tags

#Modelos
from SSAP.models import *

#Login/Logout
from django.contrib.auth import authenticate

#PDFs
from django.template.loader import get_template
from weasyprint import HTML, CSS
import os

#Pagos
import stripe
stripe.api_key = 'sk_test_51M1Iv7LIZZcOrtruCxeiGHubzCoGAoTNOP8L7P3IJZoLr2uiVHoEJoMoJPmVkgpgMqDRukfvztJnc4zdd0SSK835007fuC8e3z'

# Funciones
def func_logout(request):
    request.session.__delitem__('usuario')
    request.session.__delitem__('subtipo')

def func_login(request, usuario,subtipo):
    request.session['usuario'] = usuario
    request.session['subtipo'] = subtipo

def func_comunas(id_com=None):
    # Proceso para llenar el combobox de comuna
    opciones = ""
    ciudad = ""
    region = ""
    for ubicacion in Ubicacion.todos():
        if ubicacion.nombre_region != region:
            region = ubicacion.nombre_region
            opciones = opciones + "<option disabled>{}</option>".format(ubicacion.nombre_region)
        if ubicacion.nombre_ciudad != ciudad:
            ciudad = ubicacion.nombre_ciudad
            opciones = opciones + "<option disabled>&nbsp{}</option>".format(ubicacion.nombre_ciudad)
        if id_com == ubicacion.id_comuna:  
            opciones = opciones + "<option value={} selected>&nbsp&nbsp&nbsp{}</option>".format(ubicacion.id_comuna, ubicacion.nombre_comuna)
        else:
            opciones = opciones + "<option value={}>&nbsp&nbsp&nbsp{}</option>".format(ubicacion.id_comuna, ubicacion.nombre_comuna)
    return opciones

def func_generar_pdf(template_src, contexto, nom_archivo):
    template = get_template(template_src)
    html_tmpl = template.render(contexto)
    archivo = os.path.join(settings.BASE_DIR, nom_archivo)
    css_pag = os.path.join(settings.BASE_DIR, 'SSAP/static/css/estilo_pdf.css')
    HTML(string=html_tmpl).write_pdf(target=archivo, stylesheets=[CSS(css_pag)])

# Decoradores
def logueado(function):
    def _function(request, **kwargs):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion is None:
            return redirect('login')
        
        usuario = Usuario.filtro_id(id=usuarioSesion.id_usuario)
        if usuario.estado == False:
            request.session.__delitem__('usuario')
            messages.error(request,"Usuario deshabilitado")
            return redirect('login')
        return function(request, **kwargs)
    return _function

def esAdmin(function):
    def _function(request, **kwargs):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion.tipo != 'ADMINISTRADOR':
            return redirect('login')
        return function(request, **kwargs)
    return _function

def esCliente(function):
    def _function(request, **kwargs):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion.tipo != 'CLIENTE':
            return redirect('login')
        return function(request, **kwargs)
    return _function

def esProfesional(function):
    def _function(request, **kwargs):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion.tipo != 'PROFESIONAL':
            return redirect('login')
        return function(request, **kwargs)
    return _function

# Pruebas Wilo

def pruebas(request):
    usuario1 = Usuario.todos()
    usuario2 = Usuario.todos(orden_id=True)
    print("-------------- USUARIOS ORDENADOS POR ESTADO ----------------")
    for u in usuario1:
        print(u.id_usuario, u.direccion, u.estado)
    print("-------------- USUARIOS ORDENADOS POR ID ----------------")
    for u in usuario2:
        print(u.id_usuario, u.direccion, u.estado)
    print("-------------- CLIENTES POR ID ----------------")
    usuario = Usuario.filtro_id(id=38)
    print(Cliente.filtro_id(usuario.id_usuario).rut)
    return redirect('index')

# Vistas
#   ------------------------ Todos los Usuarios ------------------------
def login(request):
    if request.session.get('usuario') is not None:
        return redirect('index')
    if request.method=='POST':
        usuario = authenticate(request, rut=request.POST['rut'], password=request.POST['password'])
        if usuario is not None:
            tipo = None
            for cli in Cliente.todos():
                if usuario.id_usuario == cli.id_usuario:
                    tipo = cli
            for pro in Profesional.todos():
                if usuario.id_usuario == pro.id_usuario:
                    tipo = pro
            for adm in Administrador.todos():
                if usuario.id_usuario == adm.id_usuario:
                    tipo = adm
            func_login(request, usuario, tipo)
            return redirect('index')
        else:
            messages.warning(request, 'Rut o Contraseña erroneos')
    return render(request, "SSAP\login.html")

def contactanos(request):
    if request.method == 'POST':
        mails_adm = []
        for u in Usuario.todos():
            if u.tipo == 'ADMINISTRADOR':
                mails_adm.append(u.correo)
        tema = "Contacto empresa: "+ request.POST['nombre']
        mensaje = '''
        <center><h2>No más Accidentes | Contacto de empresa</h2></center>
        <hr>
        <h4><ul>
            <li>Nombre de empresa: {}</li>
            <li>Mail de Contacto: {}</li>
            <li>Numero de Teléfono: {}</li>
        </ul></h4>
        <hr>
        <h5>{}</h5>
        '''.format(request.POST['nombre'],request.POST['correo'], request.POST['telefono'], request.POST['mensaje'])
        try:
            send_mail(
                tema,
                strip_tags(mensaje),
                'no-reply.nma@outlook.com',
                mails_adm,
                fail_silently=False,
                html_message=mensaje
            )
            messages.success(request, 'Información de contacto enviada exitosamente')
        except:
            messages.error(request, 'Error: No se ha podido enviar la informacion de contacto')
        return redirect('contactanos')
    return render(request, 'SSAP/contactanos.html')

@logueado
def index(request):
    tipo = request.session.get('subtipo')
    return render(request, "SSAP\index.html",{'tipoUsuario':tipo})

@logueado
def pagLogout(request):
    func_logout(request)
    return redirect('login')

#   ------------------------ Administrador ------------------------

# Control de usuarios
@logueado
@esAdmin
def gestionUsuarios(request):
    usuarios = Usuario.todos()
    clientes = Cliente.todos()
    profesionales = Profesional.todos()
    administradores = Administrador.todos()
    return render(request,"SSAP\gestionUsuario.html", {'usr': usuarios, 'cli':clientes, 'pro':profesionales, 'adm':administradores})

@logueado
@esAdmin
def desUsuario(request):
    if request.method == 'POST':
        usuario = Usuario.filtro_id(id=request.POST['id'])
        usuario.deshabilitar()
        messages.success(request, 'Usuario '+request.POST['nombre']+' deshabilitado')
    return redirect('gestionusuario')

@logueado
@esAdmin
def habUsuario(request):
    if request.method == 'POST':
        usuario = Usuario.filtro_id(id=request.POST['id'])
        usuario.habilitar()
        messages.success(request, 'Usuario '+request.POST['nombre']+' habilitado')
    return redirect('gestionusuario')

@logueado
@esAdmin
def crearusuario(request):
    profesionales = Profesional.todos()
    # Proceso para llenar el combobox de comuna
    opciones = func_comunas()

    #Proceso para crear el Usuario
    if request.method=='POST':
        filtroRutC = Cliente.filtro_rut(rut=request.POST['username'])
        filtroRutP = Profesional.filtro_rut(rut=request.POST['username'])
        filtroRutA = Administrador.filtro_rut(rut=request.POST['username'])
        tipos = ['CLIENTE', 'PROFESIONAL','ADMINISTRADOR']
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['tipo'] not in tipos:
            messages.error(request,'Error: Tipo de usuario no admitido')
            return redirect('/crearusuario')
        if request.POST['comuna'] not in comunas:
            messages.error(request,'Error: ID de comuna no admitida')
            return redirect('/crearusuario')
        if filtroRutC is None and filtroRutP is None and filtroRutA is None:
            nuevoUsr = Usuario(
                contraseña=request.POST['password1'],
                tipo = request.POST['tipo'],
                id_comuna = request.POST['comuna'],
                direccion = request.POST['direccion'],
                correo = request.POST['email']
            )
            nuevoUsr.guardar()
            id_usr = Usuario.todos(orden_id=True)[-1].id_usuario
            if(request.POST['tipo']=='CLIENTE'):
                nuevoCli = Cliente(
                    id_usuario = id_usr,
                    rut = request.POST['username'],
                    nombre_empresa = request.POST['nombre_empresa'],
                    rubro_empresa = request.POST['rubro'],
                    cant_trabajadores = request.POST['cant_trabajadores']
                )
                nuevoCli.guardar()
                nuevoContrato = Contrato(
                    costo_base = request.POST['costo_base'],
                    fecha_firma = request.POST['fecha_firma'],
                    ultimo_pago = request.POST['fecha_firma'],
                    CLIENTE_rut = request.POST['username'],
                    PROFESIONAL_rut = request.POST['profesionalCliente']
                )
                nuevoContrato.guardar()
                idContrato = Contrato.filtro_rutcliente(request.POST['username']).id_contrato
                Checklist(id_contrato = idContrato).guardar()
                messages.success(request,'Cliente Creado')
                return redirect('/crearusuario')
            elif(request.POST['tipo']=='PROFESIONAL'):
                nuevoPro = Profesional(
                    id_usuario = id_usr,
                    rut = request.POST['username'],
                    nombre = request.POST['nombre_profesional']
                )
                nuevoPro.guardar()
                messages.success(request,'Profesional Creado')
                return redirect('/crearusuario')
            elif(request.POST['tipo']=='ADMINISTRADOR'):
                nuevoAdm = Administrador(
                    id_usuario = id_usr,
                    rut = request.POST['username'],
                    nombre = request.POST['nombre_administrador']
                )
                nuevoAdm.guardar()
                messages.success(request,'Administrador Creado')
                return redirect('/crearusuario')
        else:
            messages.error(request,'Registro Incorrecto: Rut duplicado')
            return redirect('/crearusuario')
    return render(request, "SSAP\crearusuario.html", {'profesionales':profesionales, 'ubicaciones':opciones})

@logueado
@esAdmin
def modificarUsuario(request):
    if request.method=='POST' and 'id' in request.POST:
        usuario = Usuario.filtro_id(id=request.POST['id'])
        cliente = Cliente.filtro_id(id=usuario.id_usuario)
        profesional = Profesional.filtro_id(id=usuario.id_usuario)
        administrador = Administrador.filtro_id(id=usuario.id_usuario)
        opciones = func_comunas(usuario.id_comuna)
        return render(request,"SSAP\modificarusuario.html", {'usuario':usuario, 'cliente':cliente, 'profesional':profesional,'administrador':administrador, 'comunas':opciones})
    elif request.method=='POST' and 'rutViejo' in request.POST:
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['comuna'] not in comunas:
            messages.error(request,'Error: ID de comuna no admitida')
            return redirect('gestionusuario')
        usuario = Usuario.filtro_id(id=request.POST['id_usr'])
        usuario.id_comuna = request.POST['comuna']
        usuario.contraseña = request.POST['password1']
        usuario.direccion = request.POST['direccion']
        usuario.correo = request.POST['email']
        if(usuario.tipo=='CLIENTE'):
            cliente = Cliente.filtro_id(usuario.id_usuario)
            cliente.nombre_empresa = request.POST['nombre_empresa']
            cliente.rubro_empresa = request.POST['rubro']
            cliente.cant_trabajadores = request.POST['cant_trabajadores']
            usuario.actualizar()
            cliente.actualizar()
            messages.success(request,'Cliente Modificado')
        elif(usuario.tipo=='PROFESIONAL'):
            profesional = Profesional.filtro_id(id=usuario.id_usuario)
            profesional.nombre = request.POST['nombre_profesional']
            messages.success(request,'Profesional Modificado')
            usuario.actualizar()
            profesional.actualizar()
        elif(usuario.tipo=='ADMINISTRADOR'):
            administrador = Administrador.filtro_id(usuario.id_usuario)
            administrador.nombre = request.POST['nombre_administrador']
            usuario.actualizar()
            administrador.actualizar()
            messages.success(request,'Administrador Modificado')
    return redirect('gestionusuario')

# Control de pagos
@logueado
@esAdmin
def controlPagos(request, rut):
    cliente = Cliente.filtro_rut(rut)
    if cliente is None:
        return redirect('gestionusuario')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    mensualidades = Mensualidad.todos_idcontrato(id=contrato.id_contrato)
    estado = "Al día"
    for m in mensualidades:
        if m.estado == False:
            estado = "Pendiente"
            if m.esta_atrasado():
                estado = "Atrasado"
                break
    return render(request,"SSAP\controlpagos.html", {'cliente':cliente, 'mensualidades':mensualidades, 'estado':estado})

@logueado
@esAdmin
def reportarAtraso(request):
    if request.method=='POST':
        notificacion = Notificacion(
            titulo = "Atraso en Pagos",
            descripcion = "Se le notifica que existe un pago atrasado del día {} y que puede que pronto se deshabilite su cuenta si no se realiza el pago correspondiente.".format(request.POST['fecha_limite']),
            fecha = datetime.now(),
            CLIENTE_rut = request.POST['rut_cliente']
        )
        notificacion.guardar()
        try:
            notificacion.mail()
            messages.success(request,"Notificación enviada correctamente")
        except:
            messages.warning(request,"Se envió la notificación, pero es posible que el correo no se haya enviado correctamente.")
        return redirect('/controlpagos/'+request.POST['rut_cliente'])
    return redirect('index')

@logueado
@esAdmin
def boleta_adm(request, nombre):
    archivo = str(settings.MEDIA_ROOT)+'/BOLETAS/'+nombre
    try:
        return FileResponse(open(archivo,'rb'), content_type='application/pdf')
    except:
        return redirect('index')

# Actividades
@logueado
@esAdmin
def verActividades(request):
    actividades = []
    for profesional in Profesional.todos():
        actividades = actividades+Actividad.obtener(rut=profesional.rut)
    return render(request, 'SSAP/veractividades.html',{'actividades':actividades})

# Reportería
@logueado
@esAdmin
def reportes(request):
    cant_admin = 0
    cant_prof = 0
    cant_cli = 0
    for usuario in Usuario.todos():
        if usuario.tipo == 'CLIENTE':
            cant_cli += 1
        if usuario.tipo == 'PROFESIONAL':
            cant_prof += 1
        if usuario.tipo == 'ADMINISTRADOR':
            cant_admin += 1
    datos = [cant_cli,cant_prof,cant_admin]
    script = "<script>const datos = {}; const total = {};</script>".format(datos,cant_cli+cant_admin+cant_prof)
    pagos = Pago_Mensual.todos()
    return render(request, 'SSAP/reportes.html',{'pagos':pagos, 'script':script})
#   ------------------------ Cliente ------------------------

# Notificaciones
@logueado
@esCliente
def notificaciones(request):
    cliente = request.session.get('subtipo')
    notificaciones = Notificacion.todos(cliente.rut)
    return render(request, 'SSAP/notificaciones.html', {'notificaciones':notificaciones})

@logueado
@esCliente
def elimNotif(request):
    if request.method == 'POST':
        cliente = request.session.get('subtipo')
        Notificacion.eliminar(id=request.POST['id'], rut=cliente.rut)
    return redirect('notificaciones')

# Pagos

@logueado
@esCliente
def pagos(request):
    cliente = request.session.get('subtipo')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    mensualidades = Mensualidad.todos_idcontrato(id=contrato.id_contrato)
    estado = "Al día"
    for m in mensualidades:
        if m.estado == False:
            estado = "Pendiente"
            if m.esta_atrasado():
                estado = "Atrasado"
                break
    return render(request, 'SSAP/pagos.html', {'estado':estado, 'mensualidades':mensualidades})


@logueado
@esCliente
def pagar(request):
    if request.method == 'POST':
        #Inicializar Variables
        cliente = request.session.get('subtipo')
        contrato = Contrato.filtro_rutcliente(cliente.rut)
        mensualidad = Mensualidad.filtro_id(request.POST['id'])

        #Validaciones
        ids = []
        for m in Mensualidad.todos_idcontrato(contrato.id_contrato):
            ids.append(m.id_mensualidad)
        if mensualidad.id_mensualidad not in ids:
            return redirect('pagos')
        if mensualidad.estado:
            return redirect('pagos')

        return render(request,'SSAP/procederPago.html',{'mensualidad':mensualidad})
    return redirect('pagos')

@logueado
@esCliente
def confirmarPago(request):
    if request.method == 'POST':
        #Inicializar Variables
        cliente = request.session.get('subtipo')
        contrato = Contrato.filtro_rutcliente(cliente.rut)
        mensualidad = Mensualidad.filtro_id(request.POST['id'])
        nombre_archivo = cliente.rut+str(datetime.now().strftime("%d%m%Y"))+str(mensualidad.id_mensualidad)+".pdf"
        ruta_pdf = str(settings.MEDIA_ROOT)+"/BOLETAS/"+nombre_archivo

        #Validaciones
        ids = []
        for m in Mensualidad.todos_idcontrato(contrato.id_contrato):
            ids.append(m.id_mensualidad)
        if mensualidad.id_mensualidad not in ids:
            return redirect('pagos')
        if mensualidad.estado:
            return redirect('pagos')

        #Proceder al pago
        try:
            stripe_Cliente = stripe.Customer.create(
                name = cliente.nombre_empresa,
                source = request.POST['stripeToken']
            )

            stripe.Charge.create(
                customer = stripe_Cliente,
                amount = mensualidad.costo,
                currency='clp',
                description='Renovación de contrato servicio "SSAP"'
            )
        except stripe.error.CardError as e:
            messages.error(request,'Ocurrió un error con el pago: {}'.format(e.user_message))
            return redirect('pagos')
        except stripe.error.APIConnectionError:
            messages.error(request,'Error: No se pudo conectar con stripe para pagar, intentelo más tarde.')
            return redirect('pagos')
        except:
            messages.error(request,'Ocurrió un error Inesperado, intentelo más tade.')
            return redirect('pagos')

        #Actualizar mensualidad
        mensualidad.estado = 1
        mensualidad.fecha_pago = datetime.now()
        mensualidad.boleta = nombre_archivo

        #Generar PDF boleta
        func_generar_pdf("SSAP/boleta.html",{'pago':mensualidad,'cliente':cliente},ruta_pdf)
        messages.success(request,"Pago "+str(mensualidad.fecha_limite.strftime("%d/%m/%Y"))+" realizado correctamente")
        mensualidad.actualizar()
    return redirect('pagos')

@logueado
@esCliente
def boleta_cli(request, nombre):
    cliente = request.session.get('subtipo')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    archivos = []
    for mensualidad in Mensualidad.todos_idcontrato(id=contrato.id_contrato):
        if mensualidad.boleta is not None:
            archivos.append(mensualidad.boleta)
    if nombre not in archivos:
        return redirect('pagos')
    archivo = str(settings.MEDIA_ROOT)+'/BOLETAS/'+nombre
    try:
        return FileResponse(open(archivo,'rb'), content_type='application/pdf')
    except:
        return redirect('index')
# Solicitudes

@logueado
@esCliente
def solicitudes(request):
    cliente = request.session.get('subtipo')
    cantidad_solicitudes = Cliente.filtro_rut(rut=cliente.rut).cont_solicitudes
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    solicitudes = Solicitud.todos_idcontrato(contrato.id_contrato)
    return render(request, 'SSAP/solicitudes.html', {'solicitudes':solicitudes,'cantidad_solicitudes':cantidad_solicitudes})

@logueado
@esCliente
def crearSolicitud(request):
    if request.method == "POST":
        cliente = request.session.get('subtipo')
        contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
        tipos_asesoria = ['VISITA','ACCIDENTE']
        try:
            nombre_archivo = request.FILES['archivo'].name
            #Tamaño en bytes/1000000 / tamaño en mb
            if request.FILES['archivo'].size/1000000 > 20:
                messages.error(request,"Error: Tamaño de archivo máximo: 20MB")
                return redirect('crearsolicitud')
            if not nombre_archivo.endswith(('.pdf','.rar','.zip','.png','.jpg','.jpeg','.txt')):
                messages.error(request,"Error: Tipo de archivo no admitido")
                return redirect('crearsolicitud')
            nombre_archivo = cliente.rut+str(datetime.now().strftime("%d%m%Y"))+nombre_archivo
            fs = FileSystemStorage(location=str(settings.MEDIA_ROOT)+"/SOLICITUDES/")
            fs.save(nombre_archivo, request.FILES['archivo'])
        except MultiValueDictKeyError:
            nombre_archivo = None

        if request.POST['tipo'] == "ASESORÍA":
            if request.POST['tipo_asesoria'] not in tipos_asesoria:
                return redirect('crearsolicitud')
            asesoria = Asesoria(
                tipo = "ASESORÍA",
                fecha_publicacion = datetime.now(),
                motivo = request.POST['motivo'],
                archivo = nombre_archivo,
                tipo_asesoria = request.POST['tipo_asesoria'],
                CONTRATO_id_contrato = contrato.id_contrato
            )
            asesoria.guardar()
            messages.success(request,"Asesoría del día "+str(datetime.now().strftime("%d/%m/%Y"))+" guardada.")
            return redirect('solicitudes')
        elif request.POST['tipo'] == "CAPACITACIÓN":
            solicitud_cap = SolicitudCapacitacion(
                tipo = "CAPACITACIÓN",
                fecha_publicacion = datetime.now(),
                motivo = request.POST['motivo'],
                archivo = nombre_archivo,
                CONTRATO_id_contrato = contrato.id_contrato
            )
            solicitud_cap.guardar()
            messages.success(request,"Capacitación del día "+str(datetime.now().strftime("%d/%m/%Y"))+" guardada.")
            return redirect('solicitudes')
        else:
            messages.error(request,"Tipo de solicitud no admitida")
            return redirect('solicitudes')
    return render(request, 'SSAP/crearsolicitud.html')

@logueado
@esCliente
def detalleSolicitudCli(request,id_sol):
    cliente = request.session.get('subtipo')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    tipo = None
    for soli in Solicitud.todos_idcontrato(contrato.id_contrato):
        if str(soli.id_solicitud) == id_sol:
            tipo = soli.tipo
            break
    if tipo == 'ASESORÍA':
        solicitud = Asesoria.filtro_idsolicitud(id=id_sol)
    if tipo == 'CAPACITACIÓN':
        solicitud = SolicitudCapacitacion.filtro_idsolicitud(id=id_sol)
    if not tipo:
        return redirect('solicitudes')
    return render(request, 'SSAP/detallesolicitud.html',{'solicitud':solicitud})

@logueado
@esCliente
def descargar_cli(request,nombre_archivo):
    #Validación del archivo
    cliente = request.session.get('subtipo')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    archivos = []
    for solicitud in Solicitud.todos_idcontrato(contrato.id_contrato):
        archivos.append(solicitud.archivo)
    if nombre_archivo not in archivos:
        return redirect('index')

    #Proceso de descarga del archivo
    ubicacion_archivo = str(settings.MEDIA_ROOT)+'/SOLICITUDES/'+nombre_archivo
    archivo = open(ubicacion_archivo,'rb')
    mime_type, _ = mimetypes.guess_type(ubicacion_archivo)
    response = HttpResponse(archivo, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % nombre_archivo
    return response

# Capacitaciones
@logueado
@esCliente
def capacitacionesCli(request):
    cliente = request.session.get('subtipo')
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    capacitaciones = Capacitacion.filtro_idcontrato(id=contrato.id_contrato)
    return render(request,'SSAP/capacitaciones_cli.html', {'capacitaciones':capacitaciones})

# Visitas
@logueado
@esCliente
def visitasCli(request):
    cliente = request.session.get('subtipo')
    visitas = []
    comunas = Ubicacion.todos()
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    for visita in Visita.todos():
        if visita.CONTRATO_id == contrato.id_contrato:
            visitas.append(visita)
    return render(request,'SSAP/Visitas_cli.html',{'visitas':visitas, 'comunas':comunas})

@logueado
@esCliente
def visita_cliente(request,nombre):
    archivo = str(settings.MEDIA_ROOT)+'/CHECKLISTS/'+nombre
    cliente = request.session.get('subtipo')
    nombres = []
    contrato = Contrato.filtro_rutcliente(rut=cliente.rut)
    for visita in Visita.todos():
        if visita.CONTRATO_id == contrato.id_contrato:
            nombres.append(visita.reporte_final)
    if nombre not in nombres:
        return redirect('index')
    try:
        return FileResponse(open(archivo,'rb'), content_type='application/pdf')
    except:
        return redirect('index')
#   ------------------------ Profesional ------------------------

@logueado
@esProfesional
def verClientes(request):
    profesional = request.session.get('subtipo')
    items = ""
    for c in Contrato.seleccionar_rutprofesional(profesional.rut):
        cliente = Cliente.filtro_rut(c.CLIENTE_rut)
        usuario = Usuario.filtro_id(cliente.id_usuario)
        if usuario.estado:
            items = items+"<tr><th>{}</th><th>{}</th><th>{}</th></tr>".format(cliente.rut, cliente.nombre_empresa, usuario.direccion)
    return render(request,"SSAP/verclientes.html",{'clientes':items})

# Check Lists
@logueado
@esProfesional
def checklists(request):
    profesional = request.session.get('subtipo')
    contratos = Contrato.seleccionar_rutprofesional(profesional.rut)
    items = ""
    for contrato in contratos:
        cliente = Cliente.filtro_rut(contrato.CLIENTE_rut)
        estado_cli = Usuario.filtro_id(cliente.id_usuario).estado
        elementos = Checklist.filtro_idcontrato(contrato.id_contrato).elementos
        if estado_cli:
            items = items+"<tr><th>{}</th>".format(cliente.nombre_empresa)
            if elementos:
                items = items+"<th>Con CheckList</th>"
                items = items+'''<th>
                                <div class="row esp-input">
                                    <a href="/crearchecklist/{}" class="col-sm-12"><button class="accion btn btn-primary col-sm-12">Modificar CheckList</button></a>
                                </div>
                            </th></tr>'''.format(cliente.rut)
            else:
                items = items+"<th>Sin Checklist</th>"
                items = items+'''<th>
                                <div class="row esp-input">
                                    <a href="/crearchecklist/{}" class="col-sm-12"><button class="accion btn btn-success col-sm-12">Crear CheckList</button></a>
                                </div>
                            </th></tr>'''.format(cliente.rut)
    return render(request,"SSAP/checklists.html", {'items':items})

@logueado
@esProfesional
def crearChecklist(request, rut):
    # Cargar datos para la página y verificaciones (Cliente, Checklist)
    profesional = request.session.get('subtipo')
    cliente = Cliente.filtro_rut(rut=rut)
    if cliente is None:
        return redirect('index')
    usuario = Usuario.filtro_id(cliente.id_usuario)
    contrato = Contrato.filtro_rutcliente(rut=rut)
    checklist = Checklist.filtro_idcontrato(id=contrato.id_contrato)
    items = str(checklist.elementos).split(",")
    if checklist.elementos is None:
        items = []
    if not usuario.estado or contrato.PROFESIONAL_rut != profesional.rut:
        return redirect('index')

    #Crear o Eliminar item de checklist
    if request.method=='POST' and 'item_checklist' in request.POST:
        items.append(request.POST['item_checklist'])
        checklist.elementos = ','.join(items)
        checklist.actualizar()
        return redirect(''+cliente.rut)
    if request.method=='POST' and 'id_item' in request.POST and request.POST['id_item'] in items:
        items.remove(request.POST['id_item'])
        checklist.elementos = ','.join(items)
        checklist.actualizar()
        return redirect(''+cliente.rut)
    return render(request,"SSAP/crearchecklist.html",{'checklist':items, 'cliente':cliente})

# Visitas
@logueado
@esProfesional
def visitas(request):
    profesional = request.session.get('subtipo')
    ids = []
    visitas = []
    comunas = Ubicacion.todos()
    for contrato in Contrato.seleccionar_rutprofesional(profesional.rut):
        ids.append(contrato.id_contrato)
    for visita in Visita.todos():
        if visita.CONTRATO_id in ids:
            visitas.append(visita)
    return render(request,"SSAP/visitas.html", {'visitas':visitas, 'comunas':comunas})

@logueado
@esProfesional
def programarVisita(request, id):
    profesional = request.session.get('subtipo')
    contrato = None
    visita = Visita.filtro_id(id)
    if visita is None:
        return redirect('visitas')
    for ctr in Contrato.seleccionar_rutprofesional(profesional.rut):
        if visita.CONTRATO_id == ctr.id_contrato:
            contrato = ctr
            break
    if contrato is not None and visita.estado == False:
        cliente = Cliente.filtro_rut(contrato.CLIENTE_rut)
    else:
        return redirect('visitas')
    comunas = func_comunas(visita.COMUNA_id_comuna)
    #Proceso para guardar la visita
    if request.method == 'POST':
        visita.COMUNA_id_comuna = request.POST["comuna"]
        visita.ubicacion = request.POST["ubicacion"]
        visita.fecha = datetime.strptime(request.POST["fecha"],'%Y-%m-%d')
        ultimo_dia= "{}/{}/{}".format(visita.periodo.year,visita.periodo.month,calendar.monthrange(visita.periodo.year, visita.periodo.month)[1])
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if visita.fecha < visita.periodo or visita.fecha > datetime.strptime(ultimo_dia, '%Y/%m/%d'):
            messages.error(request, "Error: Visita fuera de rango")
            return redirect('visitas')
        if visita.COMUNA_id_comuna not in comunas:
            messages.error(request, "Error: Id de comuna fuera de rango")
            return redirect('visitas')
        visita.modificar()
        notificacion = Notificacion(
            titulo = "Visita Programada/Modificada",
            descripcion = "Se le informa que se le ha programado (o modificado) una visita para el día {}. Visite el módulo de visitas para obtener más información.".format(visita.fecha.strftime('%d/%m/%Y')),
            fecha = datetime.now(),
            CLIENTE_rut = cliente.rut
        )
        notificacion.guardar()
        messages.success(request, "Visita programada")
        return redirect('visitas')
    return render(request,"SSAP/programarvisita.html",{'visita':visita, 'cliente':cliente, 'comunas':comunas})

@logueado
@esProfesional
def iniciarVisita(request, id):
    profesional = request.session.get('subtipo')
    contrato = None
    visita = Visita.filtro_id(id)
    if visita is None:
        return redirect('visitas')
    for ctr in Contrato.seleccionar_rutprofesional(profesional.rut):
        if visita.CONTRATO_id == ctr.id_contrato:
            contrato = ctr
            break
    if contrato is not None and visita.estado == False:
        cliente = Cliente.filtro_rut(contrato.CLIENTE_rut)
        checklist = Checklist.filtro_idcontrato(contrato.id_contrato)
        items = str(checklist.elementos).split(",")
        if checklist.elementos is None:
            messages.error(request,"Error: El cliente {} necesita al menos un elemento en su checklist".format(cliente.nombre_empresa))
            return redirect('visitas')
    else:
        return redirect('visitas')
    
    #Al responder la visita
    if request.method=="POST":
        #Obtener datos
        aprobados = []
        cant_aprobados = 0
        cant_maximo = 0
        cant_accidentes = cant_accidentes_mensuales(id_contrato=contrato.id_contrato,fecha=visita.periodo)
        for item in items:
            cant_maximo = cant_maximo+1
            try:
                if request.POST[item] in items:
                    cant_aprobados = cant_aprobados+1
                    aprobados.append(request.POST[item])
            except:
                None

        #Calcular datos
        mejora = request.POST["mejora"]
        porc_aprobados = round((cant_aprobados * 100)/cant_maximo,1)
        porc_reprobados = round(100 - porc_aprobados,1)
        porc_accidentabilidad = round((cant_accidentes/cliente.cant_trabajadores)*100,1)
        porc_no_accidentabilidad = round(100 - porc_accidentabilidad,1)
        barras = '''
            <div style="display: flex;">
                <div style="color:white; text-align: left  ;height: 25px; background-color: green; width: {}%;">{}%</div>
                <div style="color:white; text-align: right ;height: 25px; background-color: brown; width: {}%;">{}%</div>
            </div>
        '''.format(porc_aprobados,porc_aprobados,porc_reprobados,porc_reprobados)
        if porc_accidentabilidad <= 100:
            accidentabilidad = '''
                <ul>
                    <li class="check_success">{} Empleados</li>
                    <li class="check_fail">{} Accidentes</li>
                </ul>
                <h3>Tasa de accidentabilidad:</h3>
                <div style="display: flex;">
                    <div style="color:white; text-align: left  ;height: 25px; background-color: brown; width: {}%;">{}%</div>
                    <div style="color:white; text-align: right ;height: 25px; background-color: green; width: {}%;"></div>
                </div>
            '''.format(cliente.cant_trabajadores,cant_accidentes,porc_accidentabilidad,porc_accidentabilidad,porc_no_accidentabilidad)
        else:
            accidentabilidad = '''
                <ul>
                    <li class="check_success">{} Empleados</li>
                    <li class="check_fail">{} Accidentes</li>
                </ul>
                <h3>Tasa de accidentabilidad:</h3>
                <div style="display: flex;">
                    <div style="color:white; text-align: left  ;height: 25px; background-color: brown; width: 100%;">{}%</div>
                    <div style="color:white; text-align: right ;height: 25px; background-color: green; width: 0%;"></div>
                </div>
            '''.format(cliente.cant_trabajadores,cant_accidentes,porc_accidentabilidad)
        
        #Generar PDF
        nombre_pdf = cliente.rut+str(datetime.now().strftime("%d%m%Y"))+str(visita.id_visita)+".pdf"
        visita.reporte_final = nombre_pdf
        visita.estado = 1
        visita.modificar()
        ruta_pdf = str(settings.MEDIA_ROOT)+"/CHECKLISTS/"+nombre_pdf
        func_generar_pdf("SSAP/visitapdf.html",{'visita':visita,'cliente':cliente, 'checklist':items, 'aprobados':aprobados, 'mejora':mejora, 'barras':barras, 'accidentabilidad':accidentabilidad}, ruta_pdf)
        notificacion = Notificacion(
            titulo = "Visita {} Realizada".format(visita.fecha.strftime('%d/%m/%Y')),
            descripcion = "Se le informa que la visita del día {} ya se encuentra realizada, visite el módulo de visitas para acceder al informe.".format(visita.fecha.strftime('%d/%m/%Y')),
            fecha = datetime.now(),
            CLIENTE_rut = cliente.rut
        )
        notificacion.guardar()
        messages.success(request, "Visita "+str(visita.fecha.strftime("%d/%m/%Y"))+" realizada")
        return redirect('visitas')
    return render(request,"SSAP/iniciarvisita.html",{'visita':visita,'cliente':cliente, 'checklist':items})

@logueado
@esProfesional
def visita_profesional(request, nombre):
    archivo = str(settings.MEDIA_ROOT)+'/CHECKLISTS/'+nombre
    try:
        return FileResponse(open(archivo,'rb'), content_type='application/pdf')
    except:
        return redirect('index')

# Capacitaciones

@logueado
@esProfesional
def capacitaciones_prof(request):
    profesional = request.session.get('subtipo')
    capacitaciones = []
    for contrato in Contrato.seleccionar_rutprofesional(profesional.rut):
        capacitaciones = capacitaciones + Capacitacion.filtro_idcontrato(id=contrato.id_contrato)
    return render(request,'SSAP/capacitaciones_prof.html',{'capacitaciones':capacitaciones})

@logueado
@esProfesional
def realizarCapacitacion(request):
    if request.method == 'POST':
        # Inicializacion de datos
        capacitacion = Capacitacion.filtro_id(id=request.POST['id_capacitacion'])
        profesional = request.session.get('subtipo')
        capacitaciones = []

        # Validacion
        for contrato in Contrato.seleccionar_rutprofesional(profesional.rut):
            capacitaciones = capacitaciones + Capacitacion.filtro_idcontrato(id=contrato.id_contrato)
        ids = []
        for cap in capacitaciones:
            ids.append(cap.id_capacitacion)
        if capacitacion.id_capacitacion in ids and capacitacion.estado == 'PENDIENTE':
            # Marcar Realizada
            capacitacion.estado = 'REALIZADA'
            capacitacion.actualizar()
            messages.success(request,'Capacitación {} realizada'.format(capacitacion.nombre))
    return redirect('capacitaciones_prof')

@logueado
@esProfesional
def cancelarCapacitacion(request):
    if request.method == 'POST':
        # Inicializacion de datos
        capacitacion = Capacitacion.filtro_id(id=request.POST['id_capacitacion'])
        profesional = request.session.get('subtipo')
        capacitaciones = []

        # Validacion
        for contrato in Contrato.seleccionar_rutprofesional(profesional.rut):
            capacitaciones = capacitaciones + Capacitacion.filtro_idcontrato(id=contrato.id_contrato)
        ids = []
        for cap in capacitaciones:
            ids.append(cap.id_capacitacion)
        if capacitacion.id_capacitacion in ids and capacitacion.estado == 'PENDIENTE':
            # Marcar Cancelada
            contrato = Contrato.filtro_id(id=capacitacion.CONTRATO_id_contrato)
            capacitacion.estado = 'CANCELADA'
            capacitacion.actualizar()
            notificacion = Notificacion(
                titulo = "Capacitación {} Cancelada".format(capacitacion.fecha.strftime('%d/%m/%Y')),
                descripcion = "Se le informa que la capacitación del día {} ha sido cancelada, visite el módulo de capacitaciones para más información.".format(capacitacion.fecha.strftime('%d/%m/%Y')),
                fecha = datetime.now(),
                CLIENTE_rut = contrato.CLIENTE_rut
            )
            notificacion.guardar()
            messages.success(request,'Capacitación {} cancelada'.format(capacitacion.nombre))
    return redirect('capacitaciones_prof')

@logueado
@esProfesional
def crearCapacitacion(request):
    profesional = request.session.get('subtipo')
    clientes = []
    ruts = []
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        cliente = Cliente.filtro_rut(rut=contrato.CLIENTE_rut)
        usuario = Usuario.filtro_id(id=cliente.id_usuario)
        if usuario.estado:
            clientes.append(cliente)
            ruts.append(cliente.rut)
    comunas = func_comunas()

    #   Proceso de crear capacitacion
    if request.method == 'POST':
        # Validaciones
        if request.POST['nombre_empresa'] not in ruts:
            messages.error(request, 'Error: Rut de cliente no está en sus contratos')
            return redirect('crearCapacitacion')
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['comuna'] not in comunas:
            messages.error(request, 'Error: Id de comuna no existe')
            return redirect('crearCapacitacion')

        # Guardar capacitacion
        contrato = Contrato.filtro_rutcliente(rut=request.POST['nombre_empresa'])
        capacitacion = Capacitacion(
            nombre=request.POST['nombre'],
            ubicacion=request.POST['ubicacion'],
            fecha=datetime.strptime(request.POST['fecha'],'%Y-%m-%dT%H:%M'),
            duracion=request.POST['duracion'],
            CONTRATO_id_contrato = contrato.id_contrato,
            COMUNA_id_comuna = request.POST['comuna']
        )
        capacitacion.guardar()
        notificacion = Notificacion(
            titulo = "Nueva Capacitación",
            descripcion = "Se le informa que se realizará una capacitación el día {}, Visite el módulo de capacitaciones para más información.".format(capacitacion.fecha.strftime("%d/%m/%Y")),
            fecha = datetime.now(),
            CLIENTE_rut = request.POST['nombre_empresa']
        )
        notificacion.guardar()
        messages.success(request, 'Capacitación registrada exitosamente')
        return redirect('capacitaciones_prof')
    return render(request,'SSAP/crearCapacitacion.html', {'comunas':comunas,'clientes':clientes})

@logueado
@esProfesional
def detalleCapacitacion(request, id):
    # Inicializacion de variables
    profesional = request.session.get('subtipo')
    contratos_id = [c.id_contrato for c in Contrato.seleccionar_rutprofesional(rut=profesional.rut)]
    # Filtra si la capacitacion existe
    try:
        capacitacion = Capacitacion.filtro_id(id=id)
    except:
        return redirect('capacitaciones_prof')
    # Filtra si la capacitacion pertenece al contrato
    if capacitacion.CONTRATO_id_contrato not in contratos_id:
        return redirect('capacitaciones_prof')
    comunas = func_comunas(id_com=capacitacion.COMUNA_id_comuna)
    return render(request,'SSAP/detalleCapacitacion.html',{'capacitacion':capacitacion,'comunas':comunas})


# Solicitudes

@logueado
@esProfesional
def solicitudes_prof(request):
    profesional = request.session.get('subtipo')
    solicitudes = []
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        solicitudes = solicitudes + Solicitud.todos_idcontrato(id=contrato.id_contrato)
    return render(request,'SSAP/solicitudes_prof.html',{'solicitudes':solicitudes})

@logueado
@esProfesional
def responder_solicitud(request, id_sol):
    # Obtener datos de solicitud
    profesional = request.session.get('subtipo')
    rut_cliente = None
    id_contrato = None
    tipo = None
    comunas = func_comunas()
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        for soli in Solicitud.todos_idcontrato(id=contrato.id_contrato):
            if str(soli.id_solicitud) == id_sol:
                tipo = soli.tipo
                id_contrato = contrato.id_contrato
                rut_cliente = contrato.CLIENTE_rut
                break
    if tipo == 'ASESORÍA':
        solicitud = Asesoria.filtro_idsolicitud(id=id_sol)
    if tipo == 'CAPACITACIÓN':
        solicitud = SolicitudCapacitacion.filtro_idsolicitud(id=id_sol)

    # Filtros de solicitud
    if not tipo:
        return redirect('solicitudes_prof')
    if solicitud.estado == 'RESUELTA' or solicitud.estado == 'RECHAZADA':
        return redirect('solicitudes_prof')

    # Responder Capacitación Positivo
    if request.method == 'POST' and tipo == 'CAPACITACIÓN':
        #Validar la comuna
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['comuna'] not in comunas:
            messages.error(request, 'Error: Id de comuna no existe')
            return redirect('solicitudes_prof')

        capacitacion = Capacitacion(
            nombre=request.POST['nombre'],
            ubicacion=request.POST['ubicacion'],
            fecha=datetime.strptime(request.POST['fecha'],'%Y-%m-%dT%H:%M'),
            duracion=request.POST['duracion'],
            CONTRATO_id_contrato = id_contrato,
            COMUNA_id_comuna = request.POST['comuna']
        )
        capacitacion.guardar()
        solicitud.estado = 'RESUELTA'
        solicitud.actualizar()

        # Enviar la notificación al cliente
        notificacion = Notificacion(
            titulo = "Solicitud de Capacitación Respondida",
            descripcion = "Se le informa que una solicitud de capacitación fue respondida y la capacitación será realizada el día {}, visite el módulo de capacitaciones para más información.".format(capacitacion.fecha.strftime("%d/%m/%Y")),
            fecha = datetime.now(),
            CLIENTE_rut = rut_cliente
        )
        notificacion.guardar()

        # Descontarle la cantidad de solicitudes disponibles
        cliente = Cliente.filtro_rut(rut=rut_cliente)
        cliente.cont_solicitudes -= 1
        cliente.actualizar()
        messages.success(request, 'Capacitación creada exitosamente')
        return redirect('solicitudes_prof')
    
    #Responder Accidente
    if request.method == 'POST' and tipo == 'ASESORÍA' and solicitud.tipo_asesoria == "ACCIDENTE":
        solicitud.estado = 'RESUELTA'
        solicitud.respuesta = request.POST['respuesta_accidente']
        solicitud.actualizar()
        # Enviar la notificación al cliente
        notificacion = Notificacion(
            titulo = "Asesoría de Accidente Respondida",
            descripcion = "Se le informa que existe una respuesta al accidente ocurrido el dia {}, visite la página de solicitudes para más información.".format(solicitud.fecha_publicacion.strftime("%d/%m/%Y")),
            fecha = datetime.now(),
            CLIENTE_rut = rut_cliente
        )
        notificacion.guardar()
        messages.success(request, 'Respuesta al accidente informada al cliente')
        return redirect('solicitudes_prof')
    
    #Crear Visita Positivo
    if request.method == 'POST' and tipo == 'ASESORÍA' and solicitud.tipo_asesoria == "VISITA":
        Visita.nueva(id=id_contrato)
        solicitud.estado = 'RESUELTA'
        solicitud.respuesta = "Se ha creado una instancia de visita por programar, revise la página de visitas."
        solicitud.actualizar()

        # Enviar la notificación al cliente
        notificacion = Notificacion(
            titulo = "Asesoría de Visita Respondida",
            descripcion = "Se le informa que ya se ha creado una instancia de visita según la solicitud del día {}, visite la página de visitas para más información.".format(solicitud.fecha_publicacion.strftime("%d/%m/%Y")),
            fecha = datetime.now(),
            CLIENTE_rut = rut_cliente
        )
        notificacion.guardar()

        # Descontarle la cantidad de solicitudes disponibles
        cliente = Cliente.filtro_rut(rut=rut_cliente)
        cliente.cont_solicitudes -= 1
        cliente.actualizar()
        messages.success(request, 'Nueva instancia de visita creada exitosamente')
        return redirect('solicitudes_prof')
    return render(request,'SSAP/responder_solicitud.html',{'solicitud':solicitud,'comunas':comunas})

@logueado
@esProfesional
def descargar_prof(request,nombre_archivo):
    #Validación del archivo
    profesional = request.session.get('subtipo')
    archivos = []
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        for solicitud in Solicitud.todos_idcontrato(contrato.id_contrato):
            archivos.append(solicitud.archivo)
    if nombre_archivo not in archivos:
        return redirect('index')

    #Proceso de descarga del archivo
    ubicacion_archivo = str(settings.MEDIA_ROOT)+'/SOLICITUDES/'+nombre_archivo
    archivo = open(ubicacion_archivo,'rb')
    mime_type, _ = mimetypes.guess_type(ubicacion_archivo)
    response = HttpResponse(archivo, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % nombre_archivo
    return response

@logueado
@esProfesional
def rechazar_solicitud(request, id_sol):
    # Obtener datos de solicitud
    profesional = request.session.get('subtipo')
    rut_cliente = None
    tipo = None
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        for soli in Solicitud.todos_idcontrato(id=contrato.id_contrato):
            if str(soli.id_solicitud) == id_sol:
                tipo = soli.tipo
                rut_cliente = contrato.CLIENTE_rut
                break
    if tipo == 'ASESORÍA':
        solicitud = Asesoria.filtro_idsolicitud(id=id_sol)
        if solicitud.estado == 'PENDIENTE' and solicitud.tipo_asesoria == "VISITA":
            solicitud.estado = 'RECHAZADA'
            solicitud.respuesta = "La solicitud de visita ha sido rechazada."
            solicitud.actualizar()
            notificacion = Notificacion(
                titulo = "Asesoría de Visita Rechazada",
                descripcion = "Se le informa que su solicitud de visita del día {} ha sido rechazada, visite el módulo de solicitudes para más información.".format(solicitud.fecha_publicacion.strftime("%d/%m/%Y")),
                fecha = datetime.now(),
                CLIENTE_rut = rut_cliente
            )
            notificacion.guardar()
            messages.success(request, 'Solicitud de visita rechazada.')
    if tipo == 'CAPACITACIÓN':
        solicitud = SolicitudCapacitacion.filtro_idsolicitud(id=id_sol)
        if solicitud.estado == 'PENDIENTE':
            solicitud.estado = 'RECHAZADA'
            solicitud.actualizar()
            notificacion = Notificacion(
                titulo = "Solicitud de Capacitación Rechazada",
                descripcion = "Se le informa que su solicitud de capacitación del día {} ha sido rechazada, visite el módulo de solicitudes para más información.".format(solicitud.fecha_publicacion.strftime("%d/%m/%Y")),
                fecha = datetime.now(),
                CLIENTE_rut = rut_cliente
            )
            notificacion.guardar()
            messages.success(request, 'Solicitud de capacitación rechazada.')
    return redirect('solicitudes_prof')

@logueado
@esProfesional
def detallesolicitud_prof(request,id_sol):
    # Obtener datos de solicitud
    profesional = request.session.get('subtipo')
    tipo = None
    for contrato in Contrato.seleccionar_rutprofesional(rut=profesional.rut):
        for soli in Solicitud.todos_idcontrato(id=contrato.id_contrato):
            if str(soli.id_solicitud) == id_sol:
                tipo = soli.tipo
                break
    if tipo == 'ASESORÍA':
        solicitud = Asesoria.filtro_idsolicitud(id=id_sol)
    if tipo == 'CAPACITACIÓN':
        solicitud = SolicitudCapacitacion.filtro_idsolicitud(id=id_sol)
    if not tipo:
        return redirect('solicitudes_prof')
    return render(request, 'SSAP/detallesolicitud.html',{'solicitud':solicitud})
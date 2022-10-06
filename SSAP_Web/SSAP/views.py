#Imports
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse

#Modelos
from SSAP.models import *

#Login/Logout
from django.contrib.auth import authenticate

# Funciones
def func_logout(request):
    request.session.__delitem__('usuario')
    request.session.__delitem__('subtipo')

def func_login(request, usuario,subtipo):
    request.session['usuario'] = usuario
    request.session['subtipo'] = subtipo

# Decoradores
def logueado(function):
    def _function(request, **kwargs):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion is None:
            return redirect('login')
        
        usuario = Usuario.filtro_id(id=usuarioSesion.id_usuario)
        if usuario.estado == False:
            request.session.__delitem__('usuario')
            messages.success(request,"Usuario deshabilitado")
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
        opciones = opciones + "<option value={}>&nbsp&nbsp&nbsp{}</option>".format(ubicacion.id_comuna, ubicacion.nombre_comuna)
    
    #Proceso para crear el Usuario
    if request.method=='POST':
        filtroRutC = Cliente.filtro_rut(rut=request.POST['username'])
        filtroRutP = Profesional.filtro_rut(rut=request.POST['username'])
        filtroRutA = Administrador.filtro_rut(rut=request.POST['username'])
        tipos = ['CLIENTE', 'PROFESIONAL','ADMINISTRADOR']
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['tipo'] not in tipos:
            messages.success(request,'Error: Tipo de usuario no admitido')
            return redirect('/crearusuario')
        if request.POST['comuna'] not in comunas:
            messages.success(request,'Error: ID de comuna no admitida')
            return redirect('/crearusuario')
        if filtroRutC is None and filtroRutP is None and filtroRutA is None:
            nuevoUsr = Usuario(
                contraseña=request.POST['password1'],
                tipo = request.POST['tipo'],
                id_comuna = request.POST['comuna'],
                direccion = request.POST['direccion']
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
            messages.success(request,'Registro Incorrecto: Rut duplicado')
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
            if usuario.id_comuna == ubicacion.id_comuna:  
                opciones = opciones + "<option value={} selected>&nbsp&nbsp&nbsp{}</option>".format(ubicacion.id_comuna, ubicacion.nombre_comuna)
            else:
                opciones = opciones + "<option value={}>&nbsp&nbsp&nbsp{}</option>".format(ubicacion.id_comuna, ubicacion.nombre_comuna)
        return render(request,"SSAP\modificarusuario.html", {'usuario':usuario, 'cliente':cliente, 'profesional':profesional,'administrador':administrador, 'comunas':opciones})
    elif request.method=='POST' and 'rutViejo' in request.POST:
        comunas = ["{}".format(c.id_comuna) for c in Ubicacion.todos()]
        if request.POST['comuna'] not in comunas:
            messages.success(request,'Error: ID de comuna no admitida')
            return redirect('gestionusuario')
        usuario = Usuario.filtro_id(id=request.POST['id_usr'])
        usuario.id_comuna = request.POST['comuna']
        usuario.contraseña = request.POST['password1']
        usuario.direccion = request.POST['direccion']
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
        return redirect('/controlpagos/'+request.POST['rut_cliente'])
    return redirect('index')

@logueado
@esAdmin
def boleta_adm(request, nombre):
    archivo = 'MEDIA/BOLETAS/'+nombre
    try:
        return FileResponse(open(archivo,'rb'), content_type='application/pdf')
    except:
        return redirect('index')
#   ------------------------ Cliente ------------------------

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
                                    <a href="{}" class="col-sm-12"><button class="accion btn btn-primary col-sm-12">Modificar CheckList</button></a>
                                </div>
                            </th></tr>'''.format(contrato.id_contrato)
            else:
                items = items+"<th>Sin Checklist</th>"
                items = items+'''<th>
                                <div class="row esp-input">
                                    <a href="{}" class="col-sm-12"><button class="accion btn btn-success col-sm-12">Crear CheckList</button></a>
                                </div>
                            </th></tr>'''.format(contrato.id_contrato)
    return render(request,"SSAP/checklists.html", {'items':items})

@logueado
@esProfesional
def crearChecklist(request):
    return render(request,"SSAP/crearchecklist.html")
#Imports
from django.shortcuts import render, redirect
from django.contrib import messages

#Modelos
from SSAP.models import *

#Login/Logout
from django.contrib.auth import authenticate

#Usuarios
from django.contrib.auth.models import User

# Funciones
def func_logout(request):
    request.session.__delitem__('usuario')
    request.session.__delitem__('subtipo')

def func_login(request, usuario,subtipo):
    request.session['usuario'] = usuario
    request.session['subtipo'] = subtipo

# Decoradores
def logueado(function):
    def _function(request):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion is None:
            return redirect('login')
        
        usuario = Usuario.filtro_id(id=usuarioSesion.id_usuario)
        if usuario.estado == False:
            request.session.__delitem__('usuario')
            messages.success(request,"Usuario deshabilitado")
            return redirect('login')
        return function(request)
    return _function

def esAdmin(function):
    def _function(request):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion.tipo != 'ADMINISTRADOR':
            return redirect('login')
        return function(request)
    return _function

def esCliente(function):
    def _function(request):
        usuarioSesion = request.session.get('usuario')
        if usuarioSesion.tipo != 'CLIENTE':
            return redirect('login')
        return function(request)
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
def controlPagos(request):
    return render(request,"SSAP\controlpagos.html")

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
    if request.method=='POST':
        filtroRutC = Cliente.filtro_rut(rut=request.POST['username'])
        filtroRutP = Profesional.filtro_rut(rut=request.POST['username'])
        filtroRutA = Administrador.filtro_rut(rut=request.POST['username'])
        tipos = ['CLIENTE', 'PROFESIONAL','ADMINISTRADOR']
        if request.POST['tipo'] not in tipos:
            messages.success(request,'Error: Tipo de usuario no admitido')
            return redirect('/crearusuario')
        if filtroRutC is None and filtroRutP is None and filtroRutA is None:
            nuevoUsr = Usuario(
                contraseña=request.POST['password1'],
                tipo = request.POST['tipo'],
                id_comuna = 1,
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
    return render(request, "SSAP\crearusuario.html", {'profesionales':profesionales})

@logueado
@esAdmin
def modificarUsuario(request):
    if request.method=='POST' and 'id' in request.POST:
        usuario = Usuario.filtro_id(id=request.POST['id'])
        cliente = Cliente.filtro_id(id=usuario.id_usuario)
        profesional = Profesional.filtro_id(id=usuario.id_usuario)
        administrador = Administrador.filtro_id(id=usuario.id_usuario)
        return render(request,"SSAP\modificarusuario.html", {'usuario':usuario, 'cliente':cliente, 'profesional':profesional,'administrador':administrador})
    elif request.method=='POST' and 'rutViejo' in request.POST:
        usuario = Usuario.filtro_id(id=request.POST['id_usr'])
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
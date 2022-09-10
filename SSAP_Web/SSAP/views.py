#Imports
import imp
from pickle import TRUE
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages

#Modelos
from SSAP.models import *

#Login/Logout
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test

#Usuarios
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Formularios y funciones
class crearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12.345.678-9'}))
    password1 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '***********'}))
    password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '***********'}))
    def __init__(self, *args, **kwargs):
        super(crearForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

def esAdmin(User):
    tipoUsuario = Usuario.objects.get(rut = User.username)
    if(tipoUsuario.tipo == "ADMINISTRADOR"):
        return True
    return False

def esCliente(User):
    tipoUsuario = Usuario.objects.get(rut = User.username)
    if(tipoUsuario.tipo == "CLIENTE"):
        return True
    return False

# Vistas
#   ------------------------ Todos los Usuarios ------------------------
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method=='POST':
        usuario = authenticate(request, username=request.POST['rut'], password=request.POST['password'])
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('index')
        else:
            messages.warning(request, 'Rut o Contraseña erroneos')
    return render(request, "SSAP\login.html")

@login_required(login_url='login')
def index(request):
    tipoUsuario = Usuario.objects.get(rut = request.user.username)
    if(tipoUsuario.tipo == "CLIENTE"):
        usuario = Cliente.objects.get(rut=tipoUsuario.rut)
    elif(tipoUsuario.tipo == "PROFESIONAL"):
        usuario = Profesional.objects.get(rut=tipoUsuario.rut)
    elif(tipoUsuario.tipo == "ADMINISTRADOR"):
        usuario = Administrador.objects.get(rut=tipoUsuario.rut)
    return render(request, "SSAP\index.html",{'tipoUsuario':tipoUsuario, 'usuario':usuario})

@login_required(login_url='login')
def pagLogout(request):
    logout(request)
    return redirect('login')

#   ------------------------ Administrador ------------------------

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def gestionUsuarios(request):
    usuario = User.objects.all().exclude(is_superuser=True)
    return render(request,"SSAP\gestionUsuario.html", {'usr': usuario})

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def desUsuario(request):
    if request.method == 'POST':
        usuario = User.objects.get(username = request.POST['rut'])
        usuario.is_active = False
        usuario.save()
        messages.success(request, 'Usuario '+request.POST['rut']+' deshabilitado')
    return redirect('gestionusuario')

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def habUsuario(request):
    if request.method == 'POST':
        usuario = User.objects.get(username = request.POST['rut'])
        usuario.is_active = True
        usuario.save()
        messages.success(request, 'Usuario '+request.POST['rut']+' habilitado')
    return redirect('gestionusuario')

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def crearusuario(request):
    crearUsuario = crearForm()
    profesionales = Profesional.objects.all()
    if request.method=='POST':
        filtroRut = Usuario.objects.filter(rut=request.POST['username']).first()
        if filtroRut is None:
            crearUsuario = crearForm(request.POST)
            if crearUsuario.is_valid:
                if(request.POST['tipo']=='CLIENTE'):
                    crearUsuario.save()
                    nuevoCli = Cliente(
                        django_user=User.objects.latest('id'),
                        rut = request.POST['username'],
                        tipo = request.POST['tipo'],
                        direccion = request.POST['direccion'],
                        nombre_empresa = request.POST['nombre_empresa'],
                        rubro_empresa = request.POST['rubro'],
                        cant_trabajadores = request.POST['cant_trabajadores']
                    )
                    nuevoCli.save()
                    nuevoContrato = Contrato(
                        costo_base = request.POST['costo_base'],
                        fecha_firma = request.POST['fecha_firma'],
                        ultimo_pago = request.POST['fecha_firma'],
                        CLIENTE_rut = Cliente.objects.latest('rut'),
                        PROFESIONAL_rut = Profesional.objects.get(rut=request.POST['profesionalCliente'])
                    )
                    nuevoContrato.save()
                    messages.success(request,'Cliente Creado')
                elif(request.POST['tipo']=='PROFESIONAL'):
                    crearUsuario.save()
                    nuevoPro = Profesional(
                        django_user=User.objects.latest('id'),
                        rut = request.POST['username'],
                        tipo = request.POST['tipo'],
                        direccion = request.POST['direccion'],
                        nombre = request.POST['nombre_profesional']
                    )
                    nuevoPro.save()
                    messages.success(request,'Profesional Creado')
                elif(request.POST['tipo']=='ADMINISTRADOR'):
                    crearUsuario.save()
                    nuevoAdm = Administrador(
                        django_user=User.objects.latest('id'),
                        rut = request.POST['username'],
                        tipo = request.POST['tipo'],
                        direccion = request.POST['direccion'],
                        nombre = request.POST['nombre_administrador']
                    )
                    nuevoAdm.save()
                    messages.success(request,'Administrador Creado')
                else:
                    messages.success(request,'Error: Tipo de usuario no admitido')
                return redirect('/crearusuario')
            else:
                messages.success(request,'Registro Incorrecto: Error de Formulario')
                return redirect('/crearusuario')
        else:
            messages.success(request,'Registro Incorrecto: Rut duplicado')
            return redirect('/crearusuario')
    return render(request, "SSAP\crearusuario.html", {'crearUsuario':crearUsuario, 'profesionales':profesionales})

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def modificarUsuario(request):
    if request.method=='POST' and 'rut' in request.POST:
        usuario = User.objects.get(username=request.POST['rut'])
        return render(request,"SSAP\modificarusuario.html", {'usuario':usuario})
    elif request.method=='POST' and 'rutViejo' in request.POST:
        usuario = Usuario.objects.get(rut=request.POST['rutViejo'])
        dj_usuario = User.objects.get(username=usuario.django_user)
        if(usuario.tipo=='CLIENTE'):
            cliente = Cliente.objects.get(rut=usuario.rut)
            dj_usuario.set_password(request.POST['password1'])
            cliente.direccion = request.POST['direccion']
            cliente.nombre_empresa = request.POST['nombre_empresa']
            cliente.rubro_empresa = request.POST['rubro']
            cliente.cant_trabajadores = request.POST['cant_trabajadores']
            cliente.save()
            dj_usuario.save()
            messages.success(request,'Cliente Modificado')
        elif(usuario.tipo=='PROFESIONAL'):
            profesional = Profesional.objects.get(rut=usuario.rut)
            dj_usuario.set_password(request.POST['password1'])
            profesional.direccion = request.POST['direccion']
            profesional.nombre = request.POST['nombre_profesional']
            profesional.save()
            dj_usuario.save()
            messages.success(request,'Profesional Modificado')
        elif(usuario.tipo=='ADMINISTRADOR'):
            administrador = Administrador.objects.get(rut=usuario.rut)
            dj_usuario.set_password(request.POST['password1'])
            administrador.direccion = request.POST['direccion']
            administrador.nombre = request.POST['nombre_administrador']
            administrador.save()
            dj_usuario.save()
            messages.success(request,'Administrador Modificado')
    return redirect('gestionusuario')

#   ------------------------ Cliente ------------------------

@login_required(login_url='login')
@user_passes_test(esCliente, login_url='index')
def notificaciones(request):
    notificaciones = Notificacion.objects.filter(CLIENTE_rut = request.user.username)
    return render(request, 'SSAP/notificaciones.html', {'notificaciones':notificaciones})
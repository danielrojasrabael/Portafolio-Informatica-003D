#Imports
import imp
from pickle import TRUE
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
    tipoUsuario = Usuario.objects.get(rut = request.user.username)
    clientes = Cliente.objects.all
    profesionales = Profesional.objects.all
    administradores = Administrador.objects.all
    return render(request,"SSAP\gestionUsuario.html", {'clientes': clientes, 'profesionales': profesionales, 'administradores': administradores, 'tipoUsuario':tipoUsuario})

@login_required(login_url='login')
@user_passes_test(esAdmin, login_url='index')
def crearusuario(request):
    crearUsuario = crearForm()
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
    return render(request, "SSAP\crearusuario.html", {'crearUsuario':crearUsuario})

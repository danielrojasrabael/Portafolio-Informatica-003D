#Imports
from django.shortcuts import render, redirect
from django.contrib import messages

#Modelos
from SSAP.models import *

#Usuarios
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

#Formularios y funciones
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

#Vistas
def login(request):
    return render(request, "SSAP\login.html")

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
                        nombre = request.POST['nombre_profesional']
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
"""SSAP_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from SSAP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.pagLogout, name="logout"),
    #   ------------------------ Administrador ------------------------
    path('gestionusuario/', views.gestionUsuarios, name="gestionusuario"),
    path('desusuario', views.desUsuario, name="desusuario"),
    path('habusuario', views.habUsuario, name="habusuario"),
    path('controlpagos/', views.controlPagos, name="controlpagos"),
    path('crearusuario/', views.crearusuario, name="crearusuario"),
    path('modificarusuario/', views.modificarUsuario, name="modificarusuario"),
    #   ------------------------ Cliente ------------------------
    path('notificaciones/', views.notificaciones, name="notificaciones"),
    path('elimnotif/', views.elimNotif, name="elimnotif"),
    #   ------------------------ Profesional ------------------------
    path('verclientes/', views.verClientes, name="verclientes"),
    path('checklists/', views.checklists, name="checklists"),
    path('crearchecklist/', views.crearChecklist, name="crearchecklist"),
    path('modificarchecklist/', views.modificarChecklist, name="modificarchecklist"),
    path('visitas/', views.visitas, name="visitas"),
    path('programarvisita/', views.programarVisita, name="programarvisita"),
    #   ------------------------ Miscelaneo ------------------------
    path('pruebas/', views.pruebas, name='pruebas'),
]
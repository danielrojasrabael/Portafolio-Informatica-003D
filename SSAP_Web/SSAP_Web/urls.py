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
    path('controlpagos/<rut>', views.controlPagos, name="controlpagos"),
    path('repatraso/', views.reportarAtraso, name="repatraso/"),
    path('crearusuario/', views.crearusuario, name="crearusuario"),
    path('modificarusuario/', views.modificarUsuario, name="modificarusuario"),
    path('boleta_adm/<nombre>',views.boleta_adm, name='boleta_adm'),
    path('veractividades/',views.verActividades, name='veractividades'),
    #   ------------------------ Cliente ------------------------
    path('notificaciones/', views.notificaciones, name="notificaciones"),
    path('elimnotif/', views.elimNotif, name="elimnotif"),
    path('pagos/', views.pagos, name="pagos"),
    path('pagar/',views.pagar, name="pagar"),
    path('solicitudes/', views.solicitudes, name="solicitudes"),
    path('crearsolicitud/', views.crearSolicitud, name="crearsolicitud"),
    path('boleta_cli/<nombre>', views.boleta_cli, name="boleta_cli"),
    path('capacitaciones_cli/',views.capacitacionesCli,name='capacitaciones_cli'),
    #   ------------------------ Profesional ------------------------
    path('verclientes/', views.verClientes, name="verclientes"),
    path('checklists/', views.checklists, name="checklists"),
    path('crearchecklist/<rut>', views.crearChecklist, name="crearchecklist"),
    path('visitas/', views.visitas, name="visitas"),
    path('programarvisita/<id>', views.programarVisita, name="programarvisita"),
    path('iniciarvisita/<id>', views.iniciarVisita, name="iniciarvisita"),
    path('visita_profesional/<nombre>',views.visita_profesional,name="visita_profesional"),
    #   ------------------------ Miscelaneo ------------------------
    path('pruebas/', views.pruebas, name='pruebas'),
]
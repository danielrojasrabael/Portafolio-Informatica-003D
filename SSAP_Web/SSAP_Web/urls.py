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
    #   ------------------------ Todos ------------------------
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contactanos/', views.contactanos, name="contactanos"),
    path('login/', views.login, name="login"),
    path('logout/', views.pagLogout, name="logout"),
    path('manual/',views.manual, name="manual"),
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
    path('reportes/',views.reportes, name='reportes'),
    #   ------------------------ Cliente ------------------------
    path('notificaciones/', views.notificaciones, name="notificaciones"),
    path('elimnotif/', views.elimNotif, name="elimnotif"),
    path('pagos/', views.pagos, name="pagos"),
    path('pagar/',views.pagar, name="pagar"),
    path('solicitudes/', views.solicitudes, name="solicitudes"),
    path('crearsolicitud/', views.crearSolicitud, name="crearsolicitud"),
    path('boleta_cli/<nombre>', views.boleta_cli, name="boleta_cli"),
    path('detallesolicitud_cli/<id_sol>',views.detalleSolicitudCli,name="detallesolicitud_cli"),
    path('capacitaciones_cli/',views.capacitacionesCli,name='capacitaciones_cli'),
    path('visitas_cli/',views.visitasCli,name='visitas_cli'),
    path('visita_cliente/<nombre>',views.visita_cliente,name="visita_cliente"),
    path('descargar_cli/<nombre_archivo>',views.descargar_cli,name="descargar_cli"),
    path('confirmar_pago/',views.confirmarPago,name="confirmar_pago"),
    #   ------------------------ Profesional ------------------------
    path('verclientes/', views.verClientes, name="verclientes"),
    path('checklists/', views.checklists, name="checklists"),
    path('crearchecklist/<rut>', views.crearChecklist, name="crearchecklist"),
    path('visitas/', views.visitas, name="visitas"),
    path('programarvisita/<id>', views.programarVisita, name="programarvisita"),
    path('iniciarvisita/<id>', views.iniciarVisita, name="iniciarvisita"),
    path('visita_profesional/<nombre>',views.visita_profesional,name="visita_profesional"),
    path('capacitaciones_prof/',views.capacitaciones_prof,name='capacitaciones_prof'),
    path('realizar_capacitacion/',views.realizarCapacitacion,name='realizar_capacitacion'),
    path('cancelar_capacitacion/',views.cancelarCapacitacion,name='cancelar_capacitacion'),
    path('crearCapacitacion/',views.crearCapacitacion,name='crearCapacitacion'),
    path('detalleCapacitacion/<id>',views.detalleCapacitacion,name='detalleCapacitacion'),
    path('solicitudes_prof/', views.solicitudes_prof, name="solicitudes_prof"),
    path('responder_solicitud/<id_sol>', views.responder_solicitud, name="responder_solicitud"),
    path('descargar_prof/<nombre_archivo>',views.descargar_prof,name="descargar_prof"),
    path('rechazar_solicitud/<id_sol>',views.rechazar_solicitud,name="rechazar_solicitud"),
    path('detallesolicitud_prof/<id_sol>',views.detallesolicitud_prof,name="detallesolicitud_prof"),
    #   ------------------------ Miscelaneo ------------------------
    path('pruebas/', views.pruebas, name='pruebas'),
    ]
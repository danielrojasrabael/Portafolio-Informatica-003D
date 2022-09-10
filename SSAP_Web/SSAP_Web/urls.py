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
from API import views_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.pagLogout, name="logout"),
    path('gestionusuario/',views.gestionUsuarios, name="gestionusuario"),
    path('desusuario',views.desUsuario, name="desusuario"),
    path('habusuario',views.habUsuario, name="habusuario"),
    path('crearusuario/',views.crearusuario, name="crearusuario"),
    path('modificarusuario/',views.modificarUsuario, name="modificarusuario"),
    path('notificaciones/',views.notificaciones,name="notificaciones"),
    path('elimnotif',views.elimNotif,name="elimnotif"),
    path('api/', include('API.urls_api'))
]

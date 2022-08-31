from django.urls import include, path
from rest_framework import routers
from API import views_api

urlpatterns = [
    path('', views_api.apiOverView, name="api-overview"),

    # 1 GETs
        # 1.1 Listas

    path('admin-lista/', views_api.administradorLista, name="admin-lista"),
    path('cliente-lista/', views_api.clienteLista, name="cliente-lista"),
    path('profesional-lista/', views_api.profesionalLista, name="profesional-lista"),

        # 1.2 Elementos Singulares

    path('admin-detalle/', views_api.administradorDetalle, name="admin-detalle"),
    path('cliente-detalle/', views_api.clienteDetalle, name="cliente-detalle"),
    path('profesional-detalle/', views_api.profesionalDetalle, name="profesional-detalle"),

    # 2 POSTs

    path('admin-crear/', views_api.administradorCrear, name="admin-crear"),
    path('cliente-crear/', views_api.clienteCrear, name="cliente-crear"),
    path('profesional-crear/', views_api.profesionalCrear, name="profesional-crear"),

]
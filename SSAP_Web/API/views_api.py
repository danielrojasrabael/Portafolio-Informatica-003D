from django.shortcuts import render

# Create your views here.
from SSAP.models import Administrador, Cliente, Profesional
from django.shortcuts import render

from rest_framework import viewsets
from API.serializadores import AdministradorSerializador, ClienteSerializador, ProfesionalSerializador
from rest_framework.decorators import api_view
from rest_framework.response import Response

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all().order_by('rut')
    serializer_class = AdministradorSerializador

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('rut')
    serializer_class = ClienteSerializador

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all().order_by('rut')
    serializer_class = ProfesionalSerializador

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Metodo':'URL',
        'administradorLista':'api/admin-lista/',
        'clienteLista':'api/cliente-lista/',
        'profesionalLista':'api/profesional-lista/',
        'administradorDetalle':'api/admin-detalle/',
        'clienteDetalle':'api/cliente-detalle/',
        'profesionalDetalle':'api/profesional-detalle/',
        'administradorCrear':'api/admin-crear/',
        'clienteCrear':'api/cliente-crear/',
        'profesionalCrear':'api/profesional-crear/',
    }
    return Response(api_urls)

# 1.- --------------------------GETs--------------------------

    # 1.1.- --------------------------Listas--------------------------

@api_view(['GET'])
def administradorLista(request):
    admins = Administrador.objects.all()
    serializador = AdministradorSerializador(admins, many=True)
    return Response(serializador.data)

@api_view(['GET'])
def clienteLista(request):
    clientes = Cliente.objects.all()
    serializador = ClienteSerializador(clientes, many=True)
    return Response(serializador.data)

@api_view(['GET'])
def profesionalLista(request):
    profesionales = Profesional.objects.all()
    serializador = ProfesionalSerializador(profesionales, many=True)
    return Response(serializador.data)
    
    # 1.2.- --------------------------Elementos Singulares--------------------------

@api_view(['GET'])
def administradorDetalle(request, pk):
    admin = Administrador.objects.get(rut=pk)
    serializador = AdministradorSerializador(admin, many=False)
    return Response(serializador.data)

@api_view(['GET'])
def clienteDetalle(request, pk):
    cliente = Cliente.objects.get(rut=pk)
    serializador = ClienteSerializador(cliente, many=False)
    return Response(serializador.data)

@api_view(['GET'])
def profesionalDetalle(request, pk):
    profesional = Profesional.objects.get(rut=pk)
    serializador = ProfesionalSerializador(profesional, many=False)
    return Response(serializador.data)

# 2.- --------------------------POSTs--------------------------

@api_view(['POST'])
def administradorCrear(request):
    serializador = AdministradorSerializador(data=request.data)
    if serializador.is_valid():
        serializador.save()
    return Response(serializador.data)

@api_view(['POST'])
def clienteCrear(request):
    serializador = ClienteSerializador(data=request.data)
    if serializador.is_valid():
        serializador.save()
    return Response(serializador.data)

@api_view(['POST'])
def profesionalCrear(request):
    serializador = ProfesionalSerializador(data=request.data)
    if serializador.is_valid():
        serializador.save()
    return Response(serializador.data)
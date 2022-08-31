from rest_framework import serializers

from SSAP.models import Administrador, Cliente, Profesional

class AdministradorSerializador(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class ClienteSerializador(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProfesionalSerializador(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'
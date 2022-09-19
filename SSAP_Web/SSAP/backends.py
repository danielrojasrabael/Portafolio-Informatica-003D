from django.contrib.auth.backends import ModelBackend
from SSAP.models import Usuario, Cliente, Profesional, Administrador

class autenticar(ModelBackend):
    def authenticate(self,request,rut=None, password=None):
        
        id_usuario = None
        cliente = Cliente.filtro_rut(rut=rut)
        profesional = Profesional.filtro_rut(rut=rut)
        administrador = Administrador.filtro_rut(rut=rut)
        if cliente is not None:
            id_usuario = cliente.id_usuario
        if profesional is not None:
            id_usuario = profesional.id_usuario
        if administrador is not None:
            id_usuario = administrador.id_usuario
        if id_usuario is None:
            return None
        usuario = Usuario.filtro_id(id=id_usuario)
        if usuario.contraseña == password:
            return usuario
        return None

    def get_user(self, user_id):
        try:
            return Usuario.filtro_id(id=user_id)
        except Usuario is None:
            return None
from django.test import SimpleTestCase
from SSAP.models import *

conexion = cx_Oracle.connect(user="SSAP_TEST", password="123456", dsn="localhost:1522/ORCL1")

# -- CU 1 --

class CrearClientePrueba(SimpleTestCase):
    def setUp(self):
        #usuario = Usuario(contraseña = "1234", tipo = "CLIENTE", id_comuna = 1, direccion = "Calle Falsa")
        #usuario.guardar(conn=conexion)
        cliente = Cliente(id_usuario=1, rut="11.111.111-1", nombre_empresa="DOUC UC", rubro_empresa="educación", cant_trabajadores=2)
        cliente.guardar(conn=conexion)

    def test_creacion_cliente(self):
        cliente= Cliente.filtro_id(1, conn=conexion)
        self.assertEquals(cliente.rut, "11.111.111-1")

class DeshabilitarUsuarioPrueba(SimpleTestCase):

    def test_deshabilitar_cliente(self):
        cliente=Usuario.filtro_id(1, conn=conexion)
        cliente.deshabilitar(conn=conexion)
        cliente1=Usuario.filtro_id(1, conn=conexion)
        self.assertEquals(cliente1.estado, 0)

# -- CU 2 --


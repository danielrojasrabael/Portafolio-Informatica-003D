from django.test import SimpleTestCase
from SSAP.models import *

conexion = cx_Oracle.connect(user="SSAP_TEST", password="123456", dsn="localhost:1522/ORCL1")

# -- CU 1 --

    # -- 3 --
class CrearClientePrueba(SimpleTestCase):
    def setUp(self):
        #usuario = Usuario(contraseña = "1234", tipo = "CLIENTE", id_comuna = 1, direccion = "Calle Falsa")
        #usuario.guardar(conn=conexion)
        cliente = Cliente(id_usuario=1, rut="11.111.111-1", nombre_empresa="DOUC UC", rubro_empresa="educación", cant_trabajadores=2)
        cliente.guardar(conn=conexion)

    def test_creacion_cliente(self):
        cliente= Cliente.filtro_id(1, conn=conexion)
        self.assertEquals(cliente.rut, "11.111.111-1")

    # -- 2 --
class DeshabilitarUsuarioPrueba(SimpleTestCase):

    def test_deshabilitar_cliente(self):
        cliente=Usuario.filtro_id(1, conn=conexion)
        cliente.deshabilitar(conn=conexion)
        cliente1=Usuario.filtro_id(1, conn=conexion)
        self.assertEquals(cliente1.estado, 0)

    # -- 4 --
class ModificarUsuarioPrueba(SimpleTestCase):

    def test_modificar_cliente(self):
        cliente1 = Cliente.filtro_id(1, conn=conexion)
        cliente1.cant_trabajadores = 10
        cliente1.actualizar(conn=conexion)
        self.assertEquals(cliente1.cant_trabajadores, 10)

# -- CU 2 --

    # -- 6 --
class CrearProfesionalPrueba(SimpleTestCase):
    def setUp(self):
        #usuario = Usuario(contraseña = "1234", tipo = "CLIENTE", id_comuna = 1, direccion = "Calle Falsa")
        #usuario.guardar(conn=conexion)
        profesional = Profesional(id_usuario=21,rut="22.222.222-2",nombre="Vicente")
        profesional.guardar(conn=conexion)

    def test_creacion_profesional(self):
        profesional= Profesional.filtro_id(21, conn=conexion)
        self.assertEquals(profesional.rut, "22.222.222-2")

    # -- 5 --
class DeshabilitarProfesionalPrueba(SimpleTestCase):

    def test_deshabilitar_profesional(self):
        profesional=Usuario.filtro_id(21, conn=conexion)
        profesional.deshabilitar(conn=conexion)
        profesional1=Usuario.filtro_id(21, conn=conexion)
        self.assertEquals(profesional1.estado, 0)

    # -- 7 --
class ModificarProfesionalPrueba(SimpleTestCase):

    def test_modificar_profesional(self):
        profesional = Profesional.filtro_id(21, conn=conexion)
        profesional.nombre = "Enzo"
        profesional.actualizar(conn=conexion)
        self.assertEquals(profesional.nombre, "Enzo")
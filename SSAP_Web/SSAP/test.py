from django.test import SimpleTestCase
from SSAP.models import *

# -- CU 1 --
#  3

class CrearClientePrueba(SimpleTestCase):
    def setUp(self):
        cliente1 = Cliente(id_usuario=1, rut="11.111.111-1", nombre_empresa="DOUC UC", rubro_empresa="educación", cant_trabajadores=2)
        cliente1.guardar()

    def test_prueba_creacion_cliente(self):
        cliente1= Cliente.filtro_id(1)
        self.assertEquals(cliente1.rut, "11.111.111-1")

# -- CU 2 --

class Prueba(SimpleTestCase):
    def setUp(self):
        pass
    
    def test_prueba(self):
        numero= 2
        numeroSuma = 4
        self.assertEqual(numero+numero,numeroSuma)
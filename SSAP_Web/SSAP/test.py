from django.test import TestCase
from SSAP.models import *

'''

conn=cx_Oracle.connect(user="SSAP_TEST", password="123456", dsn="localhost:1521/XE")

# -- CU 1 --
#  3


class CrearClientePrueba(TestCase):
    def setUp(self):
        cliente1 = Cliente(id_usuario=1, rut="11.111.111-1", nombre_empresa="DOUC UC", rubro_empresa="educación", cant_trabajadores=2)
        cliente1.guardar()

    def prueba_creacion_cliente(self):
        cliente1= Cliente.filtro_id(1)
        self.assertEquals(cliente1.rut, "11.111.111-1")
# -- CU 2 -- '''

class test_prueba(TestCase):
    def setUp(self):
        pass
    
    def prueba(self):
        numero= 2
        numeroSuma = 4
        self.assertEqual(numero+numero,numeroSuma)
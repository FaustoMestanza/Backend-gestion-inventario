from django.test import TestCase
from inventario.models import Equipo

class EquipoModelTest(TestCase):

    def test_crear_equipo_minimo(self):
        equipo = Equipo.objects.create(codigo="EQ-001")
        self.assertEqual(equipo.codigo, "EQ-001")
        self.assertEqual(equipo.estado, "Disponible")

    def test_str_equipo(self):
        equipo = Equipo.objects.create(
            codigo="EQ-002",
            nombre="Laptop Lenovo"
        )
        self.assertEqual(str(equipo), "Laptop Lenovo (EQ-002)")

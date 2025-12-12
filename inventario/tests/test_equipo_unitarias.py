from django.test import TestCase
from inventario.models import Equipo

class EquipoModelTest(TestCase):

    def test_creacion_equipo_minimo(self):
        equipo = Equipo.objects.create(
            codigo="EQ-001"
        )
        self.assertEqual(equipo.codigo, "EQ-001")
        self.assertEqual(equipo.estado, "Disponible")
        self.assertIsNotNone(equipo.fecha_registro)

    def test_equipo_str(self):
        equipo = Equipo.objects.create(
            codigo="EQ-002",
            nombre="Laptop Dell"
        )
        self.assertEqual(str(equipo), "Laptop Dell (EQ-002)")

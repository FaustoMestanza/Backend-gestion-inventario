from rest_framework.test import APITestCase
from rest_framework import status
from inventario.models import Equipo

class EquipoAPITest(APITestCase):

    def setUp(self):
        self.url = "/api/equipos/"
        Equipo.objects.create(
            codigo="EQ-100",
            nombre="Proyector Epson"
        )

    def test_listar_equipos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_equipo(self):
        data = {
            "codigo": "EQ-200",
            "nombre": "Impresora HP"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filtrar_por_codigo(self):
        response = self.client.get(f"{self.url}?codigo=EQ-100")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["codigo"], "EQ-100")

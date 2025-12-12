from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from inventario.models import Equipo

class EquipoAPITest(APITestCase):

    def setUp(self):
        # Usuario de pruebas
        self.user = User.objects.create_user(
            username="testuser",
            password="test1234"
        )

        # Login JWT
        token = self.client.post(
            "/api/token/",
            {
                "username": "testuser",
                "password": "test1234"
            },
            format="json"
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token.data['access']}"
        )

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

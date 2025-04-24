from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso

class CursosTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser(
            username="admin",
            password="1234",
        )
        self.url = reverse("Cursos-list")
        self.client.force_authenticate(self.user)

        self.curso_01 = Curso.objects.create(
            nome="Dart",
            descricao="Descrição do curso Um",
            data_inicio="2023-01-01",
            data_fim="2023-12-31",
            ativo=True,
            nivel="B",
        )
        self.curso_02 = Curso.objects.create(
            nome="Python",
            descricao="Descrição do curso Dois",
            data_inicio="2023-01-01",
            data_fim="2023-12-31",
            ativo=True,
            nivel="I",
        )

    def test_requisition_get_course_list(self):
        """Test requisition get"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
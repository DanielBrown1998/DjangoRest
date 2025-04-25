from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

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

    def test_requisition_get_a_course(self):
        """Test requisition get a course with id 1"""
        response = self.client.get(f"{self.url}1/") #/cursos/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(id=1)
        data_serializer = CursoSerializer(dados_curso).data
        self.assertEqual(response.data, data_serializer)

    def test_requisition_post_for_create_course(self):
        """Test requisition post for create a course"""
        
        data = {
            "nome": "Flutter",
            "descricao": "Descrição do curso",
            "data_fim": "2026-12-31",
            "nivel": "A",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 3)
        self.assertEqual(CursoSerializer(Curso.objects.get(id=3)).data, response.data)
        
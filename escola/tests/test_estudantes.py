from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante


class EstudantesTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser(
            username="admin",
            password="1234",
        )
        self.url = reverse("Estudantes-list")
        self.client.force_authenticate(self.user)
        self.estudante_01 = Estudante.objects.create(
            nome="John Doe",
            email="john@email.com",
            cpf="56412886087",
            rg="218246328",
            data_nascimento="2000-01-01",
            telefone="11 12345-6789",
            cep="12345678",
            observacoes="Observações do estudante 01",
        )
        self.estudante_02 = Estudante.objects.create(
            nome="Jane Doe",
            email="jane@emaill.com",
            cpf="03557571092",
            rg="321343025",
            data_nascimento="2000-01-01",
            telefone="21 12345-6780",
            cep="12345679",
            observacoes="Observações do estudante 02",
        )

    def test_requisition_get_student_list(self):
        """Test requisition get"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

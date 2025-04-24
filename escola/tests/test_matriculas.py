from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.models import Matricula
from escola.models import Curso



class MatriculasTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser(
            username="admin",
            password="1234",
        )
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

        self.matricula_01 = Matricula.objects.create(
            aluno=self.estudante_01,
            curso=self.curso_01,
            matricula="202301010001",
            periodo="V"

        )
        self.matricula_02 = Matricula.objects.create(
            aluno=self.estudante_02,
            curso=self.curso_02,
            matricula="202301010002",
        )
        self.matricula_03 = Matricula.objects.create(
            aluno=self.estudante_01,
            curso=self.curso_02,
            matricula="202301010003",
        )
        self.matricula_04 = Matricula.objects.create(
            aluno=self.estudante_02,
            curso=self.curso_01,
            matricula="202301010004",
            periodo="V"
        )

        self.url = reverse("Matricula-list")
        self.client.force_authenticate(self.user)


    def test_requisition_get_matricula_list(self):
        """Test requisition get"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


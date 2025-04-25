from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

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
        response = self.client.get(self.url) #/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisition_get_a_student(self):
        """Test requisition get a student with id 1"""
        response = self.client.get(f"{self.url}1/") #/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(id=1)
        data_serializer = EstudanteSerializer(dados_estudante).data
        self.assertEqual(response.data, data_serializer)

    def test_requisition_post_for_create_student(self):
        """Test requisition post for create a student"""
        
        data = {
            "nome": "daniel",
            "email": "daniel@xpto.com",
            "cpf": "82271917034",
            "rg": "312834371",
            "data_nascimento": "1998-02-03",
            "telefone": "21985756739",
            "cep": "12345678",
        }
        # serializer = EstudanteSerializer(data=data)
        # print(serializer.is_valid())
        # print(serializer.errors)
        response = self.client.post(self.url, data) #/estudantes/
        # print(response.data)

        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
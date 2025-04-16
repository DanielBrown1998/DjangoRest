from django.test import TestCase
from escola.models import Curso, Estudante
from escola.serializers import CursoSerializer, EstudanteSerializer


class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de Modelo',
            email = 'daniel@xpto.com',
            cpf = '19033862760',
            data_nascimento = '1998-02-03',
            rg = '322820374',
            cep = '26510700',
            telefone = '21976788321'
        )


        self.serialazer_estudante = EstudanteSerializer(
            instance = self.estudante
        )


    def test_check_fields_serializers_of_student(self):
        data = self.serialazer_estudante.data

        self.assertEqual(
            set(data.keys()), 
            set([
                'nome',
                'email',
                'cpf',
                "rg",
                'data_nascimento',
                'telefone',
                'cep',
            ]))


    def test_check_content_serializers_of_student(self):
        data = self.serialazer_estudante.data

        self.assertEqual(
            set(data.values()),
            set([
                'Teste de Modelo',
                'daniel@xpto.com',
                '19033862760',
                "322820374",
                '1998-02-03',
                '21976788321',
                '26510700',
            ])
        )

from django.test import TestCase
from escola.models import Curso, Estudante

class ModelEstudanteTestCase(TestCase):
    #def test_fail(self):
    #   self.fail("Teste falhou :(")
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'daniel@xpto.com',
            cpf = '19033862760',
            data_nascimento = '1998-02-03',
            rg = '322820374',
            cep = '26510700',
            telefone = '21976788321'
        )

    def test_verifica_atributos_de_estudante(self):
        """
        Verifica os atributos do modelo de estudante!
        """
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'daniel@xpto.com')
        self.assertEqual(self.estudante.cpf, '19033862760')
        self.assertEqual(self.estudante.rg, '322820374')
        self.assertEqual(self.estudante.cep, '26510700')
        self.assertEqual(self.estudante.telefone, '21976788321')
        self.assertEqual(self.estudante.data_nascimento, '1998-02-03')



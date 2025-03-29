from django.db import models
from django.core.validators import MinLengthValidator


class Estudante(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, max_length=100)
    cpf = models.CharField(max_length=14, unique=True, blank=False)
    rg = models.CharField(max_length=12, unique=True, blank=False)
    data_nascimento = models.DateField(blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, blank=False)
    cep = models.CharField(max_length=10, blank=False)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=10, blank=False, validators=[MinLengthValidator(3)], unique=True)
    descricao = models.TextField(blank=False)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(blank=False)
    ativo = models.BooleanField(default=True)
    nivel = models.CharField(
        choices=[
            ('B', 'Básico'), 
            ('I', 'Intermediário'), 
            ('A', 'Avançado')
        ], 
        max_length=1, blank=False, null=False, default='B')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    curso = models.ForeignKey("Curso", verbose_name=("Curso"), on_delete=models.DO_NOTHING)
    aluno = models.ForeignKey("Estudante", verbose_name="Estudante", on_delete=models.DO_NOTHING)
    matricula = models.CharField(max_length=12, blank=False, null=False)
    periodo = models.CharField(
        choices = [
            ("M", "Matutino"),
            ("V", "Vespertino"),
            ("N", "Noturno"),
            ("I", "Integral"),
        ],
        max_length= 1,
        blank=False, 
        null=False, 
        default='M'
    )
    
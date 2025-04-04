import os
import django
import random

from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Curso, Matricula

dados = [
    ('CPOO1', 'Curso de Python Orientação à Objetos 01'),
    ('CPOO2', 'Curso de Python Orientação à Objetos 02'),
    ('CPOO3', 'Curso de Python Orientação à Objetos 03'),
    ('CDJ01', 'Curso de Django 01'),
    ('CDJ02', 'Curso de Django 02'),
    ('CDJ03', 'Curso de Django 03'),
    ('CDJ04', 'Curso de Django 04'),
    ('CDJ05', 'Curso de Django 05'),
    ('CDJRF01', 'Curso de Django REST Framework 01'),
    ('CDJRF02', 'Curso de Django REST Framework 02'),
    ('CDJRF03', 'Curso de Django REST Framework 03'),
    ('CDJRF04', 'Curso de Django REST Framework 04')
]

niveis = ['B', 'I', 'A']

def criar_cursos():
    Matricula.objects.all().delete()  # Limpa as matrículas existentes antes de criar novas
    Curso.objects.all().delete()  # Limpa os cursos existentes antes de criar novos
    fake = Faker('pt_BR')
    Faker.seed(10)
    for codigo, descricao in dados:
        data_fim = fake.date_between(start_date='today', end_date='+90d')
        nivel = random.choice(niveis)
        Curso.objects.create(nome=codigo, descricao=descricao, nivel=nivel, data_fim=data_fim)

criar_cursos()
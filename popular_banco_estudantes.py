import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF 
import random
from escola.models import Estudante, Matricula

def criando_pessoas(quantidade_de_pessoas):
    Matricula.objects.all().delete()  # Limpa as matrículas existentes antes de criar novas
    Estudante.objects.all().delete()  # Limpa os estudantes existentes antes de criar novos
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = fake.rg()
        cep = rg[7:].replace(".", "").replace("-", "").strip()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)  # Gera uma data de nascimento aleatória entre 18 e 30 anos
        celular = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))
        p = Estudante(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento, telefone=celular, rg=rg, cep=cep)
        p.save()

criando_pessoas(50)
from rest_framework import serializers
from escola.models import Estudante, Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = [
            'nome',
            'email',
            'cpf',
            'data_nascimento',
            'telefone',
            'cep',
            'curso',    
        ]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


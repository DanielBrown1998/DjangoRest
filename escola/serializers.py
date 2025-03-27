from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

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
        ]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'



class ListMatriculaEstudanteSerializer(serializers.ModelSerializer):

    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]
    

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListMatriculaCursoSerializer(serializers.ModelSerializer):

    estudante_nome = serializers.ReadOnlyField(source="estudante.nome")

    class Meta:
        model = Matricula
        fields = ["estudante_nome"]


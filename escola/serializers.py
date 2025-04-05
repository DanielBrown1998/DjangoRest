from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola import validators

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = [
            'nome',
            'email',
            'cpf',
        ]

    def validate(self, dados):
        if validators.cpf_invalido(dados['cpf']):
            raise serializers.ValidationError(
                {"cpf": "CPF invalido!"}
                )
        if validators.nome_invalido(dados['nome']):
            raise serializers.ValidationError(
                {"nome": "Nome so pode conter letras"}
                )
        return dados



class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = [
            'nome',
            'email',
            'cpf',
            "rg",
            'data_nascimento',
            'telefone',
            'cep',
        ]


    def validate(self, dados):
        if validators.cpf_invalido(dados['cpf']):
            raise serializers.ValidationError(
                {"cpf": "CPF invalido!"}
                )
        if validators.nome_invalido(dados['nome']):
            raise serializers.ValidationError(
                {"nome": "Nome so pode conter letras"}
                )
        if validators.telefone(dados['telefone']):
            raise serializers.ValidationError(
                {"telefone": "invalido, digite o DDD com os 9 numeros"}
                )
        if validators.cep_invalido(dados["cep"]):
            raise serializers.ValidationError(
                {"cep": "invalido, digite os 8 digitos"}
                )
        if validators.rg_invalido(dados["rg"]):
            raise serializers.ValidationError(
                {"rg": "invalido, digite os 9 digitos"}
            )
        return dados


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


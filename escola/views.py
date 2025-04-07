from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, \
    MatriculaSerializer, ListMatriculaCursoSerializer, \
        ListMatriculaEstudanteSerializer, EstudanteSerializerV2
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaThrottle
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
1
class EstudanteViewSet(viewsets.ModelViewSet):

    """
    Descricao:
     - Endpoint para CRUD Estudantes 

    Campos de ordenacao:
     - nome: permite ordenar os resultados por nome.

    Campos de busca:
    - nome: permite que a busca seja por nome.
    - cpf: permite que a busca seja por CPF.

    Metodfos HTTP:
    - POST, GET, PATCH, PUT, DELETE

    Classes Serializer:
    - EstudanteSerializer: usado para serializacao e desserializacao de dados.
    - Se a versao da APi for 'v2', usa-se EstudanteSerializerV2.
    """


    queryset = Estudante.objects.all().order_by("id")
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):

    """
    Descricao:
    - Endpoint para CRUD de cursos

    Metodos HTTP permitidos:
    - post, get, put, delete, patch  

    """

    queryset = Curso.objects.all().order_by("id")
    # queryset = Curso.objects.filter(ativo=True)
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):

    """
    Descricao:
    - Endpoint para CRUD de matriculas

    Metodos HTTP permitidos:
    - post, get
    
    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuarios anonimos.
    - UserRateThrottle: limite de taxa para usuarios autenticados

    """


    throttle_classes = [UserRateThrottle, MatriculaThrottle]
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    http_method_names = ["get", "post"] # define o smetodo de requisições que podem ser feitas

class ListMatriculaEstudante(generics.ListAPIView):

    """
    descricao da view:
    - Listar as matriculas por id de um estudante
    Parametros:
    - pk (int): identifficador primario do objeto. Deve ser um numero inteiro
    """

    serializer_class = ListMatriculaEstudanteSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"]).order_by("id")
        return queryset
    
class ListMatriculasCurso(generics.ListAPIView):

    """
    Descricao da View:
    - Listar matriculas por id de um curso
    Parametros:
    - pk (int): identifficador primario do objeto. Deve ser um numero inteiro
    """

    serializer_class = ListMatriculaCursoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"]).order_by("id")
        return queryset

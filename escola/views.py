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
    queryset = Curso.objects.all().order_by("id")
    # queryset = Curso.objects.filter(ativo=True)
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
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

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, \
    MatriculaSerializer, ListMatriculaCursoSerializer, ListMatriculaEstudanteSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

1
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    # queryset = Curso.objects.filter(ativo=True)
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListMatriculaEstudante(generics.ListAPIView):

    serializer_class = ListMatriculaEstudanteSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset
    
class ListMatriculasCurso(generics.ListAPIView):
    serializer_class = ListMatriculaCursoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

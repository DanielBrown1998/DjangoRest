from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListMatriculaEstudante, ListMatriculasCurso
from rest_framework import routers

# URL Configuration

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename="Estudantes")
router.register('cursos', CursoViewSet, basename="Cursos")
router.register("matricula", MatriculaViewSet, basename="Matricula")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("estudantes/<int:pk>/matricula/", ListMatriculaEstudante.as_view()),
    path("cursos/<int:pk>/matricula/", ListMatriculasCurso.as_view()),

]

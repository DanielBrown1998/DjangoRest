from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListMatriculaEstudante, ListMatriculasCurso
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Swagger Configuration

schema_view = get_schema_view(
    openapi.Info(
        title="Escola API",
        default_version='v1',
        description="API para gerenciamento de estudantes e cursos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="daniel@xpto.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



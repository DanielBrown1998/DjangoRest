from django.contrib import admin

from escola.models import Estudante, Curso

# Register your models here.
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'email', 'cpf', 'rg', 'ativo', 'telefone',
        'cep', 'matricula', 'curso'
    )
    list_display_links = ('id', 'cpf', 'rg')
    search_fields = ('nome', 'cpf', 'rg')   
    list_filter = ('ativo', 'data_nascimento')
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('data_cadastro',)
    list_select_related = ('curso',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'descricao', 'data_inicio', 'data_fim', 'nivel'
    )
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('nivel',)
    list_editable = ('nivel',)
    list_per_page = 10
    ordering = ('data_inicio',)
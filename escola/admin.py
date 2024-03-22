from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
# Register your models here.
class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, AlunosAdmin)

class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Curso, CursosAdmin)

class MatriculasAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
    search_fields = ('aluno',)
    list_per_page = 20

admin.site.register(Matricula, MatriculasAdmin)
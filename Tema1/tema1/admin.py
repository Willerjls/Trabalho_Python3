from django.contrib import admin
from tema1.models import Curso, Professor, Disciplina


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargaHoraria', 'ativo', 'valorMensalidade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Curso, Cursos)



class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'ativo', 'dataNascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Professor, Professores)


class Disciplinas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargaHoraria', 'professor', 'curso')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Disciplina, Disciplinas)

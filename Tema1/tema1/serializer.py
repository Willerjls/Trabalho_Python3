from rest_framework import serializers
from tema1.models import Curso, Professor, Disciplina


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class ListaDisciplinasCursoSerializer(serializers.ModelSerializer):
    curso_id = serializers.ReadOnlyField(source='curso.id')
    curso_nome = serializers.ReadOnlyField(source='curso.nome')

    class Meta:
        model = Disciplina
        fields = ['curso_id', 'curso_nome', 'nome']


class ListaDisciplinasProfessorSerializer(serializers.ModelSerializer):
    professor_id = serializers.ReadOnlyField(source='professor.id')
    professor_nome = serializers.ReadOnlyField(source='professor.nome')
    curso_nome = serializers.ReadOnlyField(source='curso.nome')

    class Meta:
        model = Disciplina
        fields = ['professor_id', 'professor_nome', 'curso_nome', 'nome']

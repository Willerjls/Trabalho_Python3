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

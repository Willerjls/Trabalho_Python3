from rest_framework import viewsets
from tema1.models import Curso, Professor, Disciplina
from tema1.serializer import CursoSerializer, ProfessorSerializer, DisciplinaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from tema1.models import Curso, Professor, Disciplina
from tema1.serializer import CursoSerializer, ProfessorSerializer, DisciplinaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from tema1.models import Curso, Professor, Disciplina
from tema1.serializer import CursoSerializer, ProfessorSerializer, DisciplinaSerializer, \
    ListaDisciplinasCursoSerializer, ListaDisciplinasProfessorSerializer


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


class ListaDisciplinasCursoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Disciplina.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaDisciplinasCursoSerializer


class ListaDisciplinasProfessorViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Disciplina.objects.filter(professor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaDisciplinasProfessorSerializer
from django.contrib import admin
from django.urls import path, include
from tema1.views import CursoViewSet, ProfessorViewSet, DisciplinaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Cursos', CursoViewSet)
router.register('Professores', ProfessorViewSet)
router.register('Disciplinas', DisciplinaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

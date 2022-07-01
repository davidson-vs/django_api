from rest_framework import routers
from .views import AlunosViewSet, CursosViewSet, MatriculasViewSet


route = routers.DefaultRouter()

alunos = route.register('alunos', viewset= AlunosViewSet, basename= 'Alunos')
cursos = route.register('cursos', viewset = CursosViewSet, basename = 'Cursos')
matriculas = route.register('matriculas', viewset = MatriculasViewSet, basename= 'Matricula')
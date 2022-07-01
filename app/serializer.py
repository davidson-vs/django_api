from pyexpat import model
from rest_framework import serializers
from app.models import Aluno, Curso, Matricula

#Estou apresentando 3 formas diferentes de trazer os campos para o json retornado.
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields ='__all__'
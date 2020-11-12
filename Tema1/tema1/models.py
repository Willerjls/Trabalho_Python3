from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()
    ativo = models.BooleanField()
    valorMensalidade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    dataNascimento = models.DateField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.


# class TodoItem(models.Model):
#     title = models.CharField(max_length=200)
#     completed = models.BooleanField(default=False)


class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class GradeCurricular(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Aula(models.Model):
    grade_curricular = models.ForeignKey(GradeCurricular, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disciplina} - {self.dia_semana} - {self.horario_inicio} - {self.horario_fim}"


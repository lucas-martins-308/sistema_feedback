from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def media_notas(self):
        feedbacks = self.feedback_set.all()
        if feedbacks:
            return round(sum([f.nota for f in feedbacks]) / feedbacks.count(), 2)
        return 0

class Feedback(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    anonimo = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('disciplina', 'aluno')

    def __str__(self):
        return f'{self.disciplina.nome} - {self.aluno.username}'

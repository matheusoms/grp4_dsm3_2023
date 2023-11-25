# No arquivo core/models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=14, default='000.000.000-00')

    def __str__(self):
        return self.nome

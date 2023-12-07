from django.db import models
    
class Plantas(models.Model):
    escolhas_dificuldade = [('Muito Fácil','Muito Fácil'),('Fácil','Fácil'),('Moderada','Moderada'),('Trabalhosa','Trabalhosa'),('Difícil','Difícil')]
    
    nome_cientifico = models.CharField(max_length=100)
    nome_popular = models.CharField(max_length=100)
    melhor_solo = models.CharField(max_length=100)
    clima = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    dificuldade_cultivar = models.CharField(max_length=100, choices=escolhas_dificuldade)
    ml_dia = models.IntegerField()
    

    def __str__(self):
        return self.nome

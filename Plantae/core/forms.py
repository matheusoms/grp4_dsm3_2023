from django import forms
from .models import Plantas
from django.core.exceptions import ValidationError

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def validacao_nome_popular(value):
    if len(value) > 15:
        raise ValidationError('O Nome Popular deve ter menos de 10 letras')
    
def validacao_clima(value):
    if len(value) > 15:
        raise ValidationError('O Clima deve ter menos de 10 letras')
    
def validacao_solo(value):
    if len(value) > 20:
        raise ValidationError('O Solo deve ter menos de 10 letras')
    
def validacao_regiao(value):
    if len(value) > 10:
        raise ValidationError('A Região deve ter menos de 10 letras')
    
def validacao_nome_cientifico(value):
    numero = contar_palavras(value)
    if numero != 2:
        raise ValidationError('O Nome Científico deve ter 2 palavras')

class PlantasForm(forms.ModelForm):
    class Meta:
        model = Plantas
        fields = ['nome_cientifico', 'nome_popular', 'melhor_solo', 'clima', 'regiao', 'dificuldade_cultivar', 'ml_dia']
        
        error_messages = {
            'nome_cientifico': {
                'required': 'Este campo é obrigatório.',
            },
            'nome_popular': {
                'required': 'Este campo é obrigatório.',
            },
            'melhor_solo': {
                'required': 'Este campo é obrigatório.',
            },
            'clima': {
                'required': 'Este campo é obrigatório.',
            },
            'regiao': {
                'required': 'Este campo é obrigatório.',
            },
            'dificuldade_cultivar': {
                'required': 'Este campo é obrigatório.',
            },
            'ml_dia': {
                'required': 'Este campo é obrigatório.',
            },
        }
        labels = {
            'nome_cientifico': 'Nome Científico',
            'nome_popular': 'Nome Popular',
            'melhor_solo': 'Melhor Solo',
            'clima': 'Clima',
            'regiao': 'Região',
            'dificuldade_cultivar': 'Dificuldade em Cultivar',
            'ml_dia': 'ML por Dia',
        }

        help_texts = {
            'nome_cientifico': 'Gênero + Espécie',
            'nome_popular': 'Nome conhecido da planta',
            'melhor_solo': 'Tipo de solo adequado para a planta',
            'clima': 'Condições climáticas ideais',
            'regiao': 'Região geográfica de origem',
            'dificuldade_cultivar': 'Nível de dificuldade para cultivar',
            'ml_dia': 'Quantidade de ML de água por dia recomendada',
        }
        
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data 
        
    def clean_nome_cientifico(self):
        valor = self.cleaned_data['nome_cientifico']
        validacao_nome_cientifico(valor)
        return valor

    def clean_nome_popular(self):
        valor = self.cleaned_data['nome_popular']
        validacao_nome_popular(valor)
        return valor

    def clean_melhor_solo(self):
        valor = self.cleaned_data['melhor_solo']
        validacao_solo(valor)
        return valor

    def clean_clima(self):
        valor = self.cleaned_data['clima']
        validacao_clima(valor)
        return valor

    def clean_regiao(self):
        valor = self.cleaned_data['regiao']
        validacao_regiao(valor)
        return valor

    
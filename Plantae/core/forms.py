# No arquivo core/forms.py
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'cpf']

    # Adicione qualquer lógica de validação personalizada aqui, se necessário
    # Por exemplo, para validar o formato do CPF
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        # Adicione sua lógica de validação aqui (por exemplo, usando uma biblioteca de validação de CPF)
        return cpf

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict

from .mongodb_utils import get_mongo_connection

from .services import criar_pessoa, obter_pessoas, obter_pessoa_por_cpf, atualizar_pessoa, excluir_pessoa
from .models import Pessoa
from .forms import PessoaForm
from django.shortcuts import redirect


def listar_pessoas(request):
    pessoas = obter_pessoas()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})


def criar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)  # Use o formulário PessoaForm
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            cpf = form.cleaned_data['cpf']
            criar_pessoa(nome, idade, cpf)  
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()  # Use o formulário PessoaForm
    return render(request, 'criar_pessoa.html', {'form': form})





def editar(request, pessoa_cpf):
    pessoa = obter_pessoa_por_cpf(pessoa_cpf)

    if pessoa:  # Verifique se a pessoa foi encontrada
        if request.method == 'POST':
            form = PessoaForm(request.POST, instance=Pessoa(**pessoa))
            if form.is_valid():
                # Adicione logs aqui
                print(f"DEBUG: Atualizando pessoa com CPF {pessoa_cpf}. Nova CPF: {form.cleaned_data['cpf']}")
                print(f"DEBUG: Documento antes da atualização: {pessoa}")
                # Atualize a pessoa no MongoDB
                atualizar_pessoa(pessoa['cpf'], form.cleaned_data['nome'], form.cleaned_data['idade'], form.cleaned_data['cpf'])
                print(f"DEBUG: Documento após da atualização: {obter_pessoa_por_cpf(form.cleaned_data['cpf'])}")
                return redirect('listar_pessoas')
        else:
            form = PessoaForm(instance=Pessoa(**pessoa))

        return render(request, 'editar_pessoa.html', {'form': form, 'pessoa_cpf': pessoa_cpf})
    else:
        # Lógica para lidar com pessoa não encontrada (por exemplo, exibir uma mensagem de erro)
        return HttpResponseNotFound("Pessoa não encontrada")

def excluir(request, pessoa_cpf):
    excluir_pessoa(pessoa_cpf)
    return redirect('listar_pessoas')

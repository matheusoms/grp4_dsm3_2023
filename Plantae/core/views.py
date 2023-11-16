from django.shortcuts import render, redirect
from .services import criar_pessoa, obter_pessoas, obter_pessoa_por_id, atualizar_pessoa, excluir_pessoa
from .forms import PessoaForm
from django.shortcuts import redirect


def listar_pessoas(request):
    pessoas = obter_pessoas()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})


def criar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            criar_pessoa(nome, idade)
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'criar_pessoa.html', {'form': form})

def editar(request, pessoa_id):
    pessoa = obter_pessoa_por_id(pessoa_id)
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            atualizar_pessoa(pessoa_id, nome, idade)
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(initial={'nome': pessoa['nome'], 'idade': pessoa['idade']})
    return render(request, 'editar_pessoa.html', {'form': form, 'pessoa_id': pessoa_id})

def excluir(request, pessoa_id):
    excluir_pessoa(pessoa_id)
    return redirect('listar_pessoas')
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render, redirect
from .services import criar_planta, excluir_planta,atualizar_planta,obter_planta_por_nome_cientifico,obter_planta
from .models import Plantas
from .forms import PlantasForm
from django.shortcuts import redirect

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def listar_plantas(request):
    plantas = obter_planta()
    return render(request, 'work.html', {'plantas': plantas})


def criar(request):
    if request.method == 'POST':
        form = PlantasForm(request.POST)
        if form.is_valid():
            nome_cientifico = form.cleaned_data['nome_cientifico']
            nome_popular = form.cleaned_data['nome_popular']
            melhor_solo = form.cleaned_data['melhor_solo']
            clima = form.cleaned_data['clima']
            regiao = form.cleaned_data['regiao']
            dificuldade_cultivar = form.cleaned_data['dificuldade_cultivar']
            ml_dia = form.cleaned_data['ml_dia']
            criar_planta(nome_cientifico,nome_popular,melhor_solo,clima,regiao,dificuldade_cultivar,ml_dia)  
            return redirect('consultar')
    else:
        form = PlantasForm()  
    return render(request, 'criar.html', {'form': form})


from django.shortcuts import render, redirect

def editar(request, nome_planta):
    resultado = obter_planta_por_nome_cientifico(nome_planta)
    
    if resultado:
        form = PlantasForm(request.POST, instance=Plantas(**resultado))

        if form.is_valid():
            atualizar_planta(
                nome_planta,
                form.cleaned_data['nome_cientifico'],
                form.cleaned_data['nome_popular'],
                form.cleaned_data['melhor_solo'],
                form.cleaned_data['clima'],
                form.cleaned_data['regiao'],
                form.cleaned_data['dificuldade_cultivar'],
                form.cleaned_data['ml_dia']
            )
            return redirect('consultar')
        else:
            return render(request, 'editar.html', {'form': form, 'nome_cientifico': nome_planta})
    else:
        return HttpResponseNotFound("Planta não encontrada")

    
def excluir(request, nome_planta):
     excluir_planta(nome_planta)
     return redirect('consultar')

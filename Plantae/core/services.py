# No arquivo core/services.py
from .forms import PlantasForm
from .mongodb_utils import get_mongo_connection

def criar_planta(nome_cientifico,nome_popular,melhor_solo,clima,regiao,dificuldade_cultivar,ml_dia):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    plantas = {"nome_cientifico": nome_cientifico, "nome_popular": nome_popular, "melhor_solo": melhor_solo, "clima": clima, "regiao": regiao, "dificuldade_cultivar": dificuldade_cultivar, "ml_dia": ml_dia}
    result = colecao.insert_one(plantas)

    client.close()
    return result.inserted_id

def obter_planta():
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']
    plantas = list(colecao.find({}, {'_id': 0}))

    client.close()
    return plantas

def obter_planta_por_nome_cientifico(busca):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    plantas_data = colecao.find_one({"nome_cientifico": busca})

    client.close()

    if plantas_data:
        plantas_data.pop('_id', None)
        print(f"DEBUG: Documento encontrado antes da atualização: {plantas_data}")
        return plantas_data
    else:
        return None

def atualizar_planta(nome_cientifico,novonome1,novonome2,novosolo,novoclima,novaregiao,novadiff,novoml):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"nome_cientifico": nome_cientifico}
    atualizacao = {"$set": {"nome_cientifico": novonome1, "nome_popular": novonome2, "melhor_solo": novosolo, "clima": novoclima, "regiao": novaregiao, "dificuldade_cultivar": novadiff, "ml_dia": novoml}}
    
    result = colecao.update_one(filtro, atualizacao)

    client.close()
    return result.modified_count


# No arquivo core/services.py

def excluir_planta(nome_planta):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"nome_cientifico": nome_planta}
    result = colecao.delete_one(filtro)

    client.close()
    return result.deleted_count


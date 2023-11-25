# No arquivo core/services.py
from .forms import PessoaForm
from .mongodb_utils import get_mongo_connection

def criar_pessoa(nome, idade, cpf):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    pessoa = {"nome": nome, "idade": idade, "cpf": cpf}
    result = colecao.insert_one(pessoa)

    client.close()
    return result.inserted_id

def obter_pessoas():
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    # Use projection para excluir o campo _id do resultado
    pessoas = list(colecao.find({}, {'_id': 0}))

    client.close()
    return pessoas

def obter_pessoa_por_cpf(pessoa_cpf):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    pessoa_data = colecao.find_one({"cpf": pessoa_cpf})

    client.close()

    if pessoa_data:
        pessoa_data.pop('_id', None)
        print(f"DEBUG: Documento encontrado antes da atualização: {pessoa_data}")
        return pessoa_data
    else:
        return None

def atualizar_pessoa(cpf, nome, idade, novo_cpf):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"cpf": cpf}
    atualizacao = {"$set": {"nome": nome, "idade": idade, "cpf": novo_cpf}}
    
    # Adicione logs temporários para depuração
    print(f"DEBUG: Atualizando pessoa com CPF {cpf}. Nova CPF: {novo_cpf}")

    result = colecao.update_one(filtro, atualizacao)

    # Adicione logs temporários para depuração
    print(f"DEBUG: Documentos modificados: {result.modified_count}")

    client.close()
    return result.modified_count


# No arquivo core/services.py

def excluir_pessoa(cpf):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"cpf": cpf}
    result = colecao.delete_one(filtro)

    client.close()
    return result.deleted_count


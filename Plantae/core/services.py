from .mongodb_utils import get_mongo_connection

def criar_pessoa(nome, idade):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    pessoa = {"nome": nome, "idade": idade}
    result = colecao.insert_one(pessoa)

    client.close()
    return result.inserted_id

def obter_pessoas():
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    pessoas = list(colecao.find())

    client.close()
    return pessoas

def obter_pessoa_por_id(pessoa_id):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    pessoa = colecao.find_one({"_id": pessoa_id})

    client.close()
    return pessoa

def atualizar_pessoa(id, nome, idade):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"_id": id}
    atualizacao = {"$set": {"nome": nome, "idade": idade}}
    result = colecao.update_one(filtro, atualizacao)

    client.close()
    return result.modified_count

def excluir_pessoa(id):
    client = get_mongo_connection()
    db = client['PROJETO']
    colecao = db['semente']

    filtro = {"_id": id}
    result = colecao.delete_one(filtro)

    client.close()
    return result.deleted_count

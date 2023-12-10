from flask import Flask,jsonify
import pymongo
import json


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False




client = pymongo.MongoClient('mongodb://localhost:27017/', unicode_decode_error_handler='ignore')
db = client['API']
colecao = db['Plantas']

  
def inserir_arquivos_json(database_name, collection_name, json_file_path):

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    database = client[database_name]


    collection = database[collection_name]

    if collection.count_documents({}) == 0:
        # Se estiver vazia, preencher com dados do arquivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            collection.insert_many(data)
        print(f"Banco {database_name} criado com sucesso.")
    else:
        print(f"A coleção {collection_name} já contém documentos.")


inserir_arquivos_json("API", "Plantas", "API.Plantas.json")

@app.route('/')
def index():
    return jsonify({
    "message": "Bem vindo a API", 
    "/plantas": "Retorna o banco completo",
    "/solo": "Retorna os dados do solo",
    "/nomes": "Retorna o nome_cientifico e nome_popular",
    "/dificuldades": "Retorna o todas as dificuldades que as plantas tem",
    "/dificuldades/<Dificuldade>": "Retorna o todas as plantas que tem a dificuldade <Dificuldade>"
    })


@app.route('/plantas')
def busca_plantas():
    try:
        dados = colecao.find({}, {'_id': 0})
        dados_lista = list(dados)
        return jsonify(dados_lista), 200, {'Content-Type': 'application/json; charset=utf-8'}  # 200 OK
    except Exception as e:
        return jsonify({"error": str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}  # 500 Internal Server Error
    



@app.route('/solo')
def busca_solo():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'solos_unicos': {'$addToSet': '$melhor_solo'}
            }
        },
        {
            '$project': {
                '_id': 0,
                'solos_unicos': 1
            }
        }
    ]

    dados = colecao.aggregate(pipeline)

    solos_unicos = next(dados)['solos_unicos']

    return jsonify({'solos_unicos': solos_unicos})

@app.route('/nome')
def busca_nome():
    dados = colecao.find({}, {'_id': 0, 'nome_cientifico': 1, 'nome_popular': 1})
    dados_lista = list(dados)
    return jsonify(dados_lista)

@app.route('/dificuldades/<dificuldade>')
def busca_dificuldade(dificuldade):
    pipeline = [
        {
            '$match': {
                'dificuldade_cultivar': dificuldade
            }
        },
        {
            '$project': {
                'dificuldade_cultivar' : 1,
                '_id': 0,
                'nome_cientifico': 1,
                'nome_popular': 1,
                'clima': 1,
                'regiao': 1,
                'ml_dia': 1,
                'melhor_solo': 1,
            },
        }
        
    ]

    resultado = list(colecao.aggregate(pipeline))
    
    resposta_json = json.dumps({'Todas as plantas com a dificuldade': dificuldade, 'resultados': resultado}, ensure_ascii=False)

    return resposta_json

@app.route('/dificuldades')
def mostrar_dificuldade():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'dificuldades_unicas': {'$addToSet': '$dificuldade_cultivar'}
            }
        },
        {
            '$project': {
                '_id': 0,
                'dificuldades_unicas': 1
            }
        }
    ]

    dados = colecao.aggregate(pipeline)

    dificuldades_unicas = next(dados)['dificuldades_unicas']
    
    resposta_json = json.dumps({'Todos os Tipos de dificuldades': dificuldades_unicas}, ensure_ascii=False)

    return resposta_json


if __name__ == '__main__':
    app.run(debug=True)
    


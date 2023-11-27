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
    "/nomes": "Retorna o nome_cientifico e nome_popular"
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
    solos = [
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

    dados = colecao.aggregate(solos)

    solos_unicos = next(dados)['solos_unicos']

    return jsonify({'solos_unicos': solos_unicos})

@app.route('/nome')
def busca_nome():
    dados = colecao.find({}, {'_id': 0, 'nome_cientifico': 1, 'nome_popular': 1})
    dados_lista = list(dados)
    return jsonify(dados_lista)

if __name__ == '__main__':
    app.run(debug=True)

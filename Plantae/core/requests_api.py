from pymongo import MongoClient
from .mongodb_utils import colecao, db
import requests

# Configurações do MongoDB
mongo_uri = "mongodb://localhost:27017/"


# URL da API
api_url = "http://127.0.0.1:5000/plantas"

# Conectar ao MongoDB
client = MongoClient(mongo_uri)
db 
colecao


def obter_dados_da_api():
    try:
        # Fazer a request para a API
        response = requests.get(api_url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Erro ao obter dados da API: {e}")
        return None

def inserir_dados_no_mongodb(dados):
    try:
        # Inserir dados no MongoDB
        colecao.insert_many(dados)
        print("Dados inseridos com sucesso no MongoDB.")
    except Exception as e:
        print(f"Erro ao inserir dados no MongoDB: {e}")

def main():
    # Obter dados da API
    dados_da_api = obter_dados_da_api()

    if dados_da_api:
        # Inserir dados no MongoDB
        inserir_dados_no_mongodb(dados_da_api)

    # Fechar a conexão com o MongoDB
    client.close()

if __name__ == "__main__":
    main()

from pymongo import MongoClient

def get_mongo_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        print("Conexão com o MongoDB estabelecida com sucesso.")
        return client
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

# Teste a conexão
mongo_client = get_mongo_connection()

# Verifique se a conexão foi bem-sucedida antes de usá-la
if mongo_client:
    # Faça o que precisa com o `mongo_client`
    db_name = 'PROJETO'
    collection_name = 'semente'

    print(f"Conectado ao banco de dados: {db_name}")
    db = mongo_client[db_name]

    print(f"Conectado à coleção: {collection_name}")
    colecao = db[collection_name]

    # ... (operações no MongoDB)
else:
    print("A conexão com o MongoDB falhou. Verifique as configurações.")

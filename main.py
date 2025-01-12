import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from llama_index.core.indices.vector_store import VectorStoreIndex, VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine


load_dotenv()

# Setup da aplicação

data_directory = os.getenv("PATH_TO_DATA")
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL_NAME")
gemini_embedding_name = os.getenv("GEMINI_EMBEDDING_NAME")
model_temperature = os.getenv("MODEL_TEMPERATURE")

# Carregamento dos arquivos presentes na pasta de dados que foi criada
documents = SimpleDirectoryReader(input_dir=data_directory)
doc = documents.load_data()

# "Criação" do modelo de linguagem Gemini e do modelo de embedding
model = Gemini(models=gemini_model, api_key=gemini_api_key)
gemini_embedding_model = GeminiEmbedding(model=gemini_embedding_name, api_key=gemini_api_key)

# Setup de configurações do RAG. Primeiro configurou-se o modelo de embedding, depois o LLM, após isso o tamanho do Chunk e por fim o overlap
Settings.embed_model = gemini_embedding_model
Settings.llm = model
Settings.chunk_size = 800
Settings.chunk_overlap = 20

# Aqui os textos se tornam vetores numéricos
index = VectorStoreIndex.from_documents(doc, show_progress=True)

# index.storage_context.persist()

# Configurando o agente de busca para buscar os 10 mais textos mais similares com o que foi passado pelo usuário
retriever = VectorIndexRetriever(index, similarity_top_k=10)
# Configurando o motor de busca
query_engine = RetrieverQueryEngine(retriever=retriever)

while True: 
    query = input("Enter query: ")
    if query == "exit":
        break
    else:
        # Passando a query para fazer a busca e já enviar para o LLM
        response = query_engine.query(query)
        print("\n"+response)
    
    print("-------------------")





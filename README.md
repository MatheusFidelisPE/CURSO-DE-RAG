# Tutorial de RAG com Llama-Index

Este projeto serve como um guia introdutório para **Retrieval-Augmented Generation (RAG)** utilizando o framework **Llama-Index**. O projeto foi desenvolvido como parte de um curso de RAG e fornece uma implementação simples para fins de aprendizado.

## Visão Geral do Projeto
Retrieval-Augmented Generation é um método que combina modelos de linguagem grandes (LLMs) com fontes de conhecimento externas, permitindo a geração de respostas baseadas em dados específicos. Este projeto demonstra:

- Configuração de um pipeline RAG com Llama-Index.
- Utilização do Gemini como provedor de LLM e embeddings.
- Consulta a um conjunto de dados personalizado para recuperar informações relevantes e gerar respostas.

## Arquivos do Projeto

### 1. `main.py`
Este é o script principal do projeto. Ele realiza as seguintes tarefas:
- Lê e carrega documentos de um diretório especificado.
- Configura as definições do Llama-Index, incluindo o LLM e o modelo de embeddings.
- Cria um índice de armazenamento vetorial a partir dos documentos.
- Configura um recuperador e um mecanismo de consulta para lidar com perguntas interativas dos usuários.

Componentes-chave no `main.py`:
- **`SimpleDirectoryReader`**: Lê o conjunto de dados do diretório `documents`.
- **`Gemini`**: O LLM usado para geração e embeddings.
- **`VectorStoreIndex`**: Armazena os embeddings dos documentos e permite a recuperação baseada em similaridade.
- **`RetrieverQueryEngine`**: Processa perguntas dos usuários recuperando informações relevantes do índice.

### 2. `.env`
Contém variáveis de ambiente para configurar o projeto:
- `GEMINI_API_KEY`: Chave de API para os serviços de LLM e embeddings do Gemini.
- `GEMINI_MODEL_NAME`: Nome do modelo LLM do Gemini.
- `GEMINI_EMBEDDING_NAME`: Nome do modelo de embeddings do Gemini.
- `PATH_TO_DATA`: Caminho para o diretório contendo os documentos a serem indexados.

## Como Executar o Projeto

### Pré-requisitos
1. Instale o Python 3.8 ou superior.
2. Instale as dependências necessárias:
   ```bash
   pip install llama-index python-dotenv
   ```
3. Certifique-se de possuir uma chave de API válida do Gemini e informações do modelo.

### Passos para Execução
1. Clone o repositório e navegue até o diretório do projeto:
   ```bash
   git clone <url-do-repositorio>
   cd <diretorio-do-projeto>
   ```
2. Configure o arquivo `.env` com as variáveis de ambiente necessárias. Exemplo:
   ```env
   GEMINI_API_KEY=sua_chave_de_api
   GEMINI_MODEL_NAME=gemini-1.5-pro
   GEMINI_EMBEDDING_NAME=models/embedding-001
   PATH_TO_DATA=./documents/
   ```
3. Adicione seus documentos na pasta `documents`.
4. Execute o script:
   ```bash
   python main.py
   ```
5. Interaja com a aplicação digitando perguntas. Digite `exit` para sair.

## Fluxo de Trabalho Exemplo
1. Coloque seu conjunto de dados na pasta `documents` (ex.: arquivos de texto).
2. Inicie a aplicação e insira uma consulta:
   ```text
   Enter query: O que é RAG?
   ```
3. Receba uma resposta baseada nos documentos indexados.

## Estrutura do Projeto
```
├── documents/         # Diretório para armazenar os documentos de entrada
├── main.py            # Script principal para executar o pipeline RAG
├── .env               # Arquivo de configuração de ambiente
└── README.md          # Documentação do projeto
```

## Notas
- O projeto foi projetado para fins educacionais e pode exigir configurações adicionais para uso em produção.
- Certifique-se de que seu conjunto de dados esteja devidamente formatado e armazenado na pasta `documents`.

## Resultados Esperados
Ao trabalhar neste projeto, você irá:
- Compreender os fundamentos de RAG e seus componentes.
- Aprender a configurar e usar o Llama-Index para construir um pipeline de consulta personalizado.
- Ganhar experiência na integração de LLMs com fontes de conhecimento externas.

---
## Vídeo para curso
Esse repositório representa a parte prática de um curso desenvolvido para a cadeira Educação à Distância. 
[RAG - Introdução e prática](https://youtube.com/playlist?list=PLXCigP7uSoCezJEMBJYovz0-Jpq3SI22s&feature=shared)


Bons estudos!


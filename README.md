# LangChain Tutorial Project

Projeto Python simples para demonstrar uso do LangChain com OpenAI e RAG (Retrieval-Augmented Generation).

## Como executar

```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o .env com sua chave da OpenAI

# Executar o projeto
python main.py
```

## Estrutura do projeto

```
.
├── main.py                     # Arquivo principal - demonstra LLMChain e RAG
├── rag.py                      # Backend RAG - funções para perguntas com contexto
├── vectordb.py                 # Carregamento e processamento de documentos
├── requirements.txt            # Dependências do projeto
├── .env.example               # Template de variáveis de ambiente
├── .env                       # Suas chaves de API (não commitado)
├── README.md                  # Este arquivo
└── .github/
    └── copilot-instructions.md # Instruções para o Copilot
```

## Funcionalidades

- **LLMChain**: Perguntas diretas ao GPT
- **RAG**: Perguntas baseadas em conteúdo web (Wikipedia)
- **Vector Database**: FAISS para busca semântica

## Requisitos

- Python 3.8+
- Chave da API da OpenAI

## diagrama de fluxo de dados

┌─────────────────┐
│     .env        │
│┌──────────────┐ │
││OPENAI_API_KEY│ │
││USER_AGENT    │ │
│└──────────────┘ │
└─────────┬───────┘
          │
          ▼
┌──────────────────┐
│    main.py       │
│                  │
│ ┌──────────────┐ │
│ │ load_dotenv()│ │
│ │ ChatOpenAI   │ │
│ │ oscar()      │ │
│ └──────────────┘ │
└─────┬─────┬──────┘
      │     │
      │     │ ask_question()
      │     ▼
      │ ┌────────────────────┐
      │ │     rag.py         │
      │ │                    │
      │ │ ┌────────────────┐ │
      │ │ │create_llm()    │ │
      │ │ │prompt_template │ │
      │ │ │create_rag_chain│ │
      │ │ └────────────────┘ │
      │ └─────────┬──────────┘
      │           │
      │           │ load_vector_db()
      │           ▼
      │ ┌────────────────────┐
      │ │   vectordb.py      │
      │ │                    │
      │ │ ┌────────────────┐ │
      │ │ │WebBaseLoader   │ │
      │ │ │OpenAIEmbeddings│ │
      │ │ │TextSplitter    │ │
      │ │ │FAISS           │ │
      │ │ └────────────────┘ │
      │ └─────────┬──────────┘
      │           │
      │           ▼
      │ ┌──────────────────┐
      │ │   Wikipedia      │
      │ │ Oppenheimer Page │
      │ └──────────────────┘
      │
      ▼
┌─────────────────┐
│   Terminal      │
│   Output        │
│                 │
│ LLMChain: X     │
│ RAG: Y          │
└─────────────────┘
🤖 RAG Chat Interface
Retrieval-Augmented Generation com interface web moderna usando Streamlit
Interface intuitiva para fazer perguntas sobre documentos PDF ou conteúdo web, utilizando modelos de IA locais (Ollama) ou na nuvem (OpenAI).

🚀 Como executar
bash# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações

# Executar aplicação web
streamlit run main.py

📁 Estrutura do projeto
📦 rag-chat-interface/
├── 📄 main.py                     # Interface Streamlit - App principal
├── 🧠 rag.py                      # Motor RAG - Processamento de perguntas
├── 🗃️ vectordb.py                 # Banco vetorial - FAISS + embeddings
├── 📋 requirements.txt            # Dependências Python
├── 🔧 .env.example               # Template de configuração
├── 📖 README.md                  # Documentação do projeto
├── 📂 .github/
│   └── 📝 copilot-instructions.md # Instruções para GitHub Copilot
└── 📂 __pycache__/               # Cache Python (auto-gerado)

✨ Funcionalidades
🏠 Ollama Local

🤖 Modelos executados localmente
📄 Processamento de PDFs
🌐 Análise de conteúdo web
🔒 Privacidade total dos dados

☁️ OpenAI Cloud

🚀 GPT-4 via API
📊 Processamento otimizado
🌍 Acesso global
⚡ Respostas rápidas

🎯 Recursos Técnicos

Vector Database: FAISS para busca semântica
Text Splitting: Chunks inteligentes para melhor contexto
Dual Processing: Local (Ollama) + Cloud (OpenAI)
File Handling: Upload seguro de PDFs com limpeza automática
Web Scraping: Extração de conteúdo de URLs


🛠️ Tecnologias
ComponenteTecnologiaInterfaceStreamlitLLM LocalOllama (Gemma 12B)LLM CloudOpenAI GPT-4o-miniEmbeddingsOpenAI + Snowflake ArcticVector DBFAISSPDF ParserPyPDFWeb LoaderLangChain WebBase

🔧 Configuração
Arquivo .env
env# OpenAI (para modo nuvem)
OPENAI_API_KEY=sua_chave_aqui

# Ollama (para modo local)
OLLAMA_BASE_URL=http://localhost:11434

# Configurações gerais
USER_AGENT=rag-chat-interface
Modelos Ollama
bash# Instalar modelos necessários
ollama pull gemma3:12b
ollama pull snowflake-arctic-embed2:latest

🎮 Como usar

Escolha o modo: Ollama (local) ou OpenAI (nuvem)
Selecione a fonte: PDF upload ou URL
Faça sua pergunta: Digite o que deseja saber
Obtenha respostas: Contextualizadas com o documento

💡 Exemplos de uso

"Resuma os pontos principais deste PDF"
"Quais são as conclusões do artigo?"
"Explique o conceito mencionado na página X"


🔄 Fluxo de Dados
mermaidgraph TD
    A[👤 Usuário] --> B[🖥️ Interface Streamlit]
    B --> C{📁 Fonte?}
    
    C -->|PDF| D[📄 Upload + Temp File]
    C -->|URL| E[🌐 Web Scraping]
    
    D --> F[🔤 Text Splitting]
    E --> F
    
    F --> G[🧮 Embeddings]
    G --> H[🗃️ Vector Store FAISS]
    
    H --> I{🤖 Modelo?}
    I -->|Local| J[🏠 Ollama]
    I -->|Cloud| K[☁️ OpenAI]
    
    J --> L[💬 Resposta]
    K --> L
    
    L --> B
    B --> A

🧪 Arquitetura RAG
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   📄 Document   │ -> │  🔤 Text Split   │ -> │ 🧮 Embeddings  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         v                        v                        v
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ 🗃️ Vector Store │ <- │ 🔍 Similarity    │ <- │ ❓ User Query   │
└─────────────────┘    │    Search        │    └─────────────────┘
         │              └──────────────────┘                │
         v                        │                        v
┌─────────────────┐              v              ┌─────────────────┐
│ 📝 Context      │ -----------> 🤖 LLM ------> │ 💬 Answer      │
└─────────────────┘              Model          └─────────────────┘

📋 Requisitos

Python: 3.8+
Ollama: Para execução local
OpenAI API: Para modo nuvem
Dependências: Ver requirements.txt


🚧 Desenvolvimento
Estrutura de Códigos

main.py: Interface Streamlit com abas e controles
rag.py: Lógica RAG, templates de prompt e chains
vectordb.py: Carregamento de documentos e criação de embeddings

Padrões utilizados

✅ Separação de responsabilidades
✅ Funções modulares reutilizáveis
✅ Gerenciamento seguro de arquivos temporários
✅ Tratamento de diferentes fontes de dados
✅ Interface responsiva e intuitiva


🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades!

🎯 Transforme documentos em conversas inteligentes!
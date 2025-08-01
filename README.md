<div align="center">
🚀 Interface RAG Chat
"Onde Documentos Encontram Inteligência"
Transforme documentos estáticos em conversas dinâmicas com IA de ponta

🎯 Demo • ⚡ Início Rápido • 📖 Documentação • 🤝 Contribuir

</div>
🌟 O Que Torna Isso Especial?
<table> <tr> <td width="50%">
🏠 Filosofia Local-First
🔒 Zero Vazamento de Dados - Seus documentos nunca saem da sua máquina

🚀 Ultra Rápido - Modelos Ollama executam localmente

💰 Custo Zero - Sem custos de API para processamento local

🛡️ Privacidade por Design - Controle total dos seus dados

</td> <td width="50%">
☁️ Poder da Nuvem Disponível
🧠 Inteligência GPT-4 - Acesso aos modelos mais avançados

🌍 Escala Global - Processe documentos de qualquer lugar

⚡ Performance Otimizada - Inferência ultra-rápida na nuvem

🔄 Troca Perfeita - Alterne entre local/nuvem instantaneamente

</td> </tr> </table>
🎯 Demo
mermaid
Copiar
Editar
graph LR
    A[📄 Upload PDF] --> B[🤖 Escolha Modelo IA]
    B --> C[❓ Faça Pergunta]
    C --> D[💡 Resposta Inteligente]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
De Documento a Insight em 30 Segundos
⚡ Início Rápido
<details> <summary><b>🔧 Configuração em Um Clique</b></summary>
bash
Copiar
Editar
# 🚀 Clone & Configure
git clone <seu-repositorio>
cd rag-chat-interface

# 📦 Instalar Dependências
pip install -r requirements.txt

# 🔑 Configurar Ambiente
cp .env.example .env
# Adicione suas chaves API no .env

# 🎬 Executar Aplicação
streamlit run main.py
🎉 Pronto! Sua interface RAG está online em http://localhost:8501

</details> <details> <summary><b>🐳 Deploy Rápido com Docker</b></summary>
bash
Copiar
Editar
# 🏗️ Build & Execute
docker build -t rag-chat .
docker run -p 8501:8501 rag-chat

# 🌐 Acesse em localhost:8501
</details>
🏗️ Arquitetura
mermaid
Copiar
Editar
flowchart TD
    subgraph "🖥️ Camada Frontend"
        A[Interface Streamlit] 
        B[Upload de Arquivos]
        C[Interface Chat]
    end
    
    subgraph "🧠 Camada Processamento"
        D[Parser Documentos]
        E[Divisor de Texto]
        F[Motor Embeddings]
    end
    
    subgraph "🗃️ Camada Armazenamento"
        G[FAISS Vector DB]
        H[Arquivos Temporários]
    end
    
    subgraph "🤖 Camada IA"
        I[Ollama Local]
        J[OpenAI Nuvem]
    end
    
    A --> D
    B --> D
    D --> E
    E --> F
    F --> G
    G --> I
    G --> J
    I --> C
    J --> C
📁 Estrutura do Projeto
graphql
Copiar
Editar
📦 rag-chat-interface/
├── main.py                     # Interface Streamlit
├── rag.py                      # Motor RAG
├── vectordb.py                 # Banco Vetorial
├── requirements.txt            # Dependências
├── .env.example                # Configuração de Ambiente
├── README.md                   # Documentação
├── .gitignore                  # Git Ignore
├── .github/
│   └── copilot-instructions.md # Diretrizes IA
└── __pycache__/                # Cache Python
🎮 Showcase de Recursos
<table> <tr> <td width="33%">
📄 Processamento Inteligente de PDF
🔍 Parsing Inteligente

✂️ Divisão Otimizada

🏷️ Preservação de Metadados

🚀 Processamento em Lote

</td> <td width="33%">
🌐 Análise de Conteúdo Web
🕷️ Scraping Inteligente

🔗 Validação de URL

📊 Filtragem de Conteúdo

🔄 Tempo Real

</td> <td width="33%">
🧮 Inteligência Vetorial
🎯 Busca Semântica

📐 Pontuação de Similaridade

💾 Armazenamento FAISS

⚡ Respostas Rápidas

</td> </tr> </table>
🛠️ Stack Tecnológica
Categoria	Tecnologia	Propósito
🎨 Frontend	Streamlit	Interface Web Interativa
🧠 LLM Local	Ollama	Modelos Locais Privados
☁️ LLM Nuvem	OpenAI	IA de Nuvem Avançada
🔗 Framework	LangChain	Framework de Aplicações IA
🗃️ Banco Vetorial	FAISS	Busca por Similaridade
📄 Parser PDF	PyPDF	Processamento de Documentos
🌐 Web Scraper	WebLoader	Extração de Conteúdo da Web

⚙️ Configuração
<details> <summary><b>🔐 Configuração de Ambiente</b></summary>
env
Copiar
Editar
# 🌟 Configuração OpenAI (Modo Nuvem)
OPENAI_API_KEY=sk-sua-chave-secreta-aqui
OPENAI_MODEL=gpt-4o-mini

# 🏠 Configuração Ollama (Modo Local)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_LLM_MODEL=gemma3:12b
OLLAMA_EMBED_MODEL=snowflake-arctic-embed2:latest

# 🌐 Configurações Gerais
USER_AGENT=rag-chat-interface/1.0
LOG_LEVEL=INFO
MAX_FILE_SIZE=50MB
</details> <details> <summary><b>🤖 Configuração dos Modelos Ollama</b></summary>
bash
Copiar
Editar
# 📥 Baixar Modelos
ollama pull gemma3:12b
ollama pull snowflake-arctic-embed2:latest

# 🔍 Verificar Instalação
ollama list

# 🚀 Iniciar Serviço
ollama serve
</details>
🎯 Guia de Uso
🚀 Começando em 3 Passos
1️⃣ Escolha Sua IA – Aba Ollama ou OpenAI
2️⃣ Envie Seu Conteúdo – Upload de PDF ou URL
3️⃣ Comece a Conversa – Faça perguntas e receba respostas

💡 Casos de Uso
<details> <summary><b>📚 Pesquisa Acadêmica</b></summary>
Resumos de seções

Revisão de literatura

Interpretação estatística

Esclarecimento de conceitos

</details> <details> <summary><b>📋 Inteligência de Negócios</b></summary>
Análise de relatórios

Pesquisa de mercado

Insights estratégicos

Análise competitiva

</details> <details> <summary><b>📖 Aprendizado Pessoal</b></summary>
Resumos de livros

Geração de quiz

Explicações simples

Conexão entre ideias

</details>
🚀 Recursos Avançados
mermaid
Copiar
Editar
mindmap
  root((Recursos RAG))
    Processamento Inteligente
      Divisão Inteligente
      Preservação Contexto
      Extração Metadados
    Suporte Multi-Modal
      Documentos PDF
      Conteúdo Web
      Arquivos Texto
    Flexibilidade IA
      Modelos Locais
      APIs Nuvem
      Troca de Modelos
    Segurança Primeiro
      Limpeza Arquivos Temp
      Proteção Privacidade
      Processamento Seguro
📊 Métricas de Performance
Métrica	Local (Ollama)	Nuvem (OpenAI)
🚀 Tempo Resposta	10–40 segundos	2–5 segundos
💰 Custo por Query	R$ 0,00	~R$ 0,01
🔒 Nível Privacidade	100% Privado	Processamento Nuvem
📊 Qualidade da Resposta	5,5/10	9,5/10

🔧 Desenvolvimento
<details> <summary><b>🏗️ Configuração Desenvolvimento Local</b></summary>
bash
Copiar
Editar
git clone <seu-fork>
cd rag-chat-interface

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

pip install -r requirements.txt
pip install -r requirements-dev.txt

pytest tests/
black .
isort .

streamlit run main.py --server.runOnSave true
</details> <details> <summary><b>📁 Organização do Código</b></summary>
python
Copiar
Editar
# main.py - UI
# rag.py - lógica IA
# vectordb.py - camada vetorial
</details>
🤝 Contribuição
🌟 Adoramos Contribuidores!
<details> <summary><b>🎯 Como Contribuir</b></summary>
Fork

Nova branch (feature/recurso-incrivel)

Code & teste

Commit (git commit -m 'Adiciona recurso incrível')

Push

Pull Request

</details> <details> <summary><b>💡 Ideias de Contribuição</b></summary>
Melhorias UI/UX

Suporte a novos modelos

Dashboard

Suporte multi-idioma

Segurança avançada

Otimização para mobile

</details>
📜 Licença
Este projeto está licenciado sob a Licença MIT

🙏 Agradecimentos
🚀 Construído com amor e IA

Transformando a maneira como interagimos com documentos, uma pergunta por vez.
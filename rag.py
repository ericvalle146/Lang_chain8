# Templates para formatação de prompts enviados ao LLM
from langchain_core.prompts import ChatPromptTemplate

# Criação de chains para recuperação de informações (RAG)
from langchain.chains import create_retrieval_chain

# Função para carregar banco vetorial
from vectordb import load_vector_db_url, load_vector_db_pdf, load_vector_db_url_local, load_vector_db_pdf_local

# Cliente para conectar com OpenAI GPT
from langchain_openai import ChatOpenAI

# Cliente para conectar com Ollama local
from langchain_ollama import ChatOllama

# Carregamento de variáveis de ambiente (.env)
from dotenv import load_dotenv

# Proteção das credenciais
import os

load_dotenv()

def create_model_openai():
    """Cria e configura o modelo de linguagem OpenAI."""
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


def create_model_ollama():
    """Cria e configura o modelo de linguagem Ollama local."""
    return ChatOllama(model="gemma3:12b", base_url=os.getenv("OLLAMA_BASE_URL"), temperature=0.2)


def create_prompt_template():
    """Cria o template de prompt para o sistema RAG."""
    return ChatPromptTemplate.from_template("""
    Responda a pergunta com base no contexto fornecido.
                                            
    Contexto: {context}
    
    Question: {input}
    """)

def create_rag_url(url):
    """Cria a cadeia completa RAG para uma URL específica."""
    llm = create_model_openai()
    prompt = create_prompt_template()
    retriever = load_vector_db_url(url)
    # document_chain = create_stuff_documents_chain(llm, prompt)
    document_chain = prompt | llm
    return create_retrieval_chain(retriever, document_chain)


def ask_question_url(url, question):
    """Faz uma pergunta sobre o conteúdo de uma URL usando RAG."""
    chain = create_rag_url(url)
    response = chain.invoke({"input": question})
    return response["answer"].content


def create_rag_pdf(pdf):
    """Cria a cadeia completa RAG para um PDF específico."""
    llm = create_model_openai()
    prompt = create_prompt_template()
    retriever = load_vector_db_pdf(pdf)
    
    document_chain = prompt | llm
    return create_retrieval_chain(retriever, document_chain)


def ask_question_pdf(pdf, question):
    """Faz uma pergunta sobre o conteúdo de um PDF usando RAG."""
    chain = create_rag_pdf(pdf)
    response = chain.invoke({"input": question})
    return response["answer"].content


def create_rag_url_local(url):
    """Cria a cadeia completa RAG para uma URL específica. Local"""
    llm = create_model_ollama()
    prompt = create_prompt_template()
    retriever = load_vector_db_url_local(url)

    document_chain = prompt | llm
    return create_retrieval_chain(retriever, document_chain)


def ask_question_url_local(url, question):
    """Faz uma pergunta sobre o conteúdo de uma URL usando RAG. Local"""
    chain = create_rag_url_local(url)
    response = chain.invoke({"input": question})
    return response["answer"].content


def create_rag_pdf_local(pdf):
    """Cria a cadeia completa RAG para um PDF específico. Local"""
    llm = create_model_ollama()
    prompt = create_prompt_template()
    retriever = load_vector_db_pdf_local(pdf)
    
    document_chain = prompt | llm
    return create_retrieval_chain(retriever, document_chain)


def ask_question_pdf_local(pdf, question):
    """Faz uma pergunta sobre o conteúdo de um PDF usando RAG. Local"""
    chain = create_rag_pdf_local(pdf)
    response = chain.invoke({"input": question})
    return response["answer"].content



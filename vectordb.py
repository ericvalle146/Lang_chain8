# Carregamento de conteúdo web
from langchain_community.document_loaders import WebBaseLoader

# Carregamento de documento pdf
from langchain_community.document_loaders import PyPDFLoader

# Criação de embeddings com OpenAI
from langchain_openai import OpenAIEmbeddings

# Criação de embeddings com Ollama local
from langchain_ollama.embeddings import OllamaEmbeddings

# Banco vetorial para busca semântica
from langchain_community.vectorstores import FAISS

# Divisão de textos em chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configuração de variáveis de ambiente
import os
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('USER_AGENT', 'langchain-tutorial')


def load_vector_db_url(url):
    """Carrega documentos de uma URL e cria retriever vetorial."""
    loader = WebBaseLoader(url)
    data = loader.load()
    
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
    documents = text_splitter.split_documents(data)
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever()

    

def load_vector_db_pdf(pdf):
    """Carrega documentos de um PDF e cria retriever vetorial."""
    loader = PyPDFLoader(pdf)
    data = loader.load()
    
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
    documents = text_splitter.split_documents(data)
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever()



def load_vector_db_url_local(url):
    """Carrega documentos de uma URL e cria retriever vetorial."""
    loader = WebBaseLoader(url)
    data = loader.load()
    
    embeddings = OllamaEmbeddings(model="snowflake-arctic-embed2:latest", base_url=os.getenv("OLLAMA_BASE_URL"))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
    documents = text_splitter.split_documents(data)
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever()

    

def load_vector_db_pdf_local(pdf):
    """Carrega documentos de um PDF e cria retriever vetorial."""
    loader = PyPDFLoader(pdf)
    data = loader.load()
    
    embeddings = OllamaEmbeddings(model="snowflake-arctic-embed2:latest", base_url=os.getenv("OLLAMA_BASE_URL"))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
    documents = text_splitter.split_documents(data)
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever()

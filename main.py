# Carregamento da interface 
import streamlit as st

# Carregamento de variáveis de ambiente (.env)
from dotenv import load_dotenv

# Função para perguntas com RAG
from rag import ask_question_url , ask_question_pdf, ask_question_url_local, ask_question_pdf_local

# Criar arquivos temporários
import tempfile

# Operações do sistema, deletar arquivos temporários
import os
load_dotenv()



if __name__ == "__main__":
    
    # Paginas
    pagina_ollama, pagina_openai = st.tabs(["Ollama", "OpenAI"])

    # Pagina modelos Ollama
    with pagina_ollama:
        st.title("Chat RAG - OLLAMA")
        fonte = st.selectbox("Fonte de conhecimento:", ["PDF", "URL"])
        pdf = st.file_uploader("PDF", type="pdf") if fonte == "PDF" else None
        url = st.text_input("URL", placeholder="Cole aqui a URL...") if fonte == "URL" else None
        pergunta = st.text_input("Pergunta:", placeholder="Digite sua pergunta...")
        
        # Processamento 
        if st.button("Enviar"):

            # RAG PDF
            if fonte == "PDF" and pdf:

                # PDF temporario
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                    tmp.write(pdf.getvalue())
                    # Gravação disco
                    tmp.flush()

                    # Requisição llm
                    st.write(ask_question_pdf_local(tmp.name, pergunta))

                    # Remover arquivo
                    os.unlink(tmp.name)
            # RAG URL
            elif url:
                st.write(ask_question_url_local(url, pergunta))

    # Pagina modelos Openai
    with pagina_openai:
        st.title("Chat RAG - OPENAI")
        fonte2 = st.selectbox("Fonte:", ["PDF", "URL"], key="f2")
        pdf2 = st.file_uploader("PDF", type="pdf", key="p2") if fonte2 == "PDF" else None
        url2 = st.text_input("URL", placeholder="Cole aqui a URL...", key="u2") if fonte2 == "URL" else None
        pergunta2 = st.text_input("Pergunta:", placeholder="Digite sua pergunta...", key="q2")
        
        # Processamento
        if st.button("Enviar", key="b2"):

            # RAG PDF
            if fonte2 == "PDF" and pdf2:

                # PDF temporario
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                    tmp.write(pdf2.getvalue())
                    tmp.flush()

                    # Requisição llm
                    st.write(ask_question_pdf(tmp.name, pergunta2))

                    # Remover arquivo
                    os.unlink(tmp.name)
            # RAG URL
            elif url2:
                st.write(ask_question_url(url2, pergunta2))
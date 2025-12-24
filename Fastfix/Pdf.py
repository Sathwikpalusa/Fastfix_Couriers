from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()



docs=PyPDFLoader("Fastfix.pdf")
docs1=docs.load()
documents=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50).split_documents(docs1)
embeddings=OllamaEmbeddings(model="tinyllama")
db=FAISS.from_documents(documents,embeddings)
st.title("Welcome to Fastfix couriers")
llm=Ollama(model="tinyllama")
prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions carefully on courier services based on the following pdf, this is my business
    and answer based on the given context and chat history given below. If you dont know the answer just tell me you dont know about the following topcic.
    <chathistory>
    {chathistory}
    <chathistory>
    <context>
    {context}
    <context>
    Questions:{input}

    """
    
)
document_chain=create_stuff_documents_chain(llm,prompt)
retriver=db.as_retriever()
retrival_chain=create_retrieval_chain(retriver,document_chain)
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

user_input=st.text_input("Ask anything about Fastfix")


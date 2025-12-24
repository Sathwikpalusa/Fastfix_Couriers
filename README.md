# 🚚 Fastfix Couriers – RAG-Based AI Assistant

Fastfix Couriers AI Assistant is a **Retrieval-Augmented Generation (RAG) web application** built using **Streamlit** and **LangChain**.  
It allows users to ask natural language questions about Fastfix Couriers’ services and get **accurate, context-aware answers** strictly based on the company’s internal PDF document.

The application uses **session-based conversational memory** to support follow-up questions and maintain chat continuity.

---

## 🧠 Features

- PDF-based knowledge ingestion using LangChain loaders  
- Semantic text chunking for better retrieval accuracy  
- Vector-based document search using FAISS  
- Retrieval-Augmented Generation (RAG) for grounded responses  
- Session-based chat memory using Streamlit  
- Local LLM inference using Ollama  
- Simple and intuitive web interface  

---

## 🏗️ Architecture Flow

1. PDF Document Loader (Fastfix.pdf)  
2. Recursive Text Chunking  
3. Embedding Generation  
4. FAISS Vector Store  
5. Retriever for relevant context  
6. LLM-based Answer Generation  
7. Session Memory for chat history  
8. Streamlit UI  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- Ollama (LLM & Embeddings)  
- FAISS (Vector Store)  
- dotenv  

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/fastfix-rag-app.git
cd fastfix-rag-app
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py

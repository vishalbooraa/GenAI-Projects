# 🤖 RAG Chatbot with LangChain & ChromaDB

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to build an intelligent chatbot capable of answering questions based on **local PDF documents**.

The system combines **semantic search + Large Language Models (LLMs)** to generate accurate, context-aware responses.

---

## 🚀 Features

* 📄 **PDF Ingestion:** Automatically loads and processes PDF files
* ✂️ **Document Chunking:** Uses `RecursiveCharacterTextSplitter` for optimal splitting
* 🧠 **Semantic Embeddings:** Powered by `all-MiniLM-L6-v2` (Sentence Transformers)
* 🗄️ **Vector Storage:** Persistent storage using **ChromaDB**
* 🔍 **Contextual Retrieval:** Fetches Top-K relevant chunks using similarity search
* 🤖 **LLM Integration:** Uses **Groq (Llama 3.1)** for fast response generation

---

## 🛠️ Technical Stack

* **Framework:** LangChain
* **LLM:** Llama-3.1-8b *(via Groq API)*
* **Vector Database:** ChromaDB
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Processing:** PyPDFLoader, Scikit-learn

---

## 📋 Pipeline Workflow

1. **Ingestion**

   * Load PDFs from `/data` directory

2. **Chunking**

   * Split documents into **500-character chunks** with **50 overlap**

3. **Embedding**

   * Convert text into **384-dimensional vectors**

4. **Storage**

   * Store embeddings in persistent **ChromaDB collection**

5. **Retrieval**

   * Retrieve most relevant chunks using similarity search

6. **Generation**

   * Send query + context to LLM → generate final answer

---

## ⚙️ Setup & Usage

### 1. Install Dependencies

```bash id="v92k0n"
pip install langchain langchain-groq chromadb sentence-transformers pypdf scikit-learn
```

---

### 2. Configuration

* Create a `data/` folder in the root directory
* Add your PDF files inside it
* Set your **Groq API Key** in the notebook or environment

---

### 3. Run the Project

This project is implemented as a **Jupyter Notebook**:

```bash id="e6q5u7"
chatbot_using_rag.ipynb
```

Run cells step-by-step to:

* Initialize embedding and vector store
* Index your documents
* Query your chatbot

---

## 🧪 Example Usage

```python
answer = generate_output("What are the main paradigms of RAG?", rag_retriever, llm)
print(answer)
```

---

## 📊 Features in Action

* Context-aware answers from your own documents
* Fast retrieval using vector similarity
* Scalable pipeline for multiple PDFs

---

## 🧠 Future Improvements

* Add Streamlit UI for interactive chatbot
* Support multi-document sources (web, APIs)
* Implement hybrid search (BM25 + embeddings)
* Add chat history memory

---

## 🤝 Contribution

Contributions are welcome!

* Improve retrieval strategies
* Experiment with different LLMs
* Optimize chunking & embeddings

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vishal Boora**
B.Tech IT (2026) | AI/ML & GenAI Developer

---

# RAG Learning Assistant

Production-grade Retrieval-Augmented Generation (RAG) application built with FastAPI, OpenAI Embeddings, ChromaDB, and GPT-4o-mini.

This project demonstrates how modern AI systems combine semantic search, vector databases, and large language models to deliver grounded and context-aware answers from custom knowledge sources.

Designed as an enterprise-style AI Engineering project for scalable educational and knowledge retrieval applications.


## Overview

Traditional Large Language Models generate responses based only on their training data.

Retrieval-Augmented Generation (RAG) enhances LLMs by retrieving relevant information from external documents before generating a response.

This project allows users to:

* Upload documents
* Convert documents into embeddings
* Store embeddings in ChromaDB
* Perform semantic search
* Retrieve relevant context
* Generate grounded answers using GPT-4o-mini

The result is a more accurate and reliable AI assistant that can answer questions based on specific knowledge sources.


## Architecture

User Question
│
▼
FastAPI Endpoint (/ask)
│
▼
Semantic Search
│
▼
ChromaDB Vector Store
│
▼
Relevant Context Retrieval
│
▼
GPT-4o-mini
│
▼
Grounded Response

## Features

* Retrieval-Augmented Generation (RAG)
* OpenAI Embeddings
* ChromaDB Vector Database
* Semantic Search
* FastAPI REST API
* Configurable Environment Variables
* Modular Enterprise Architecture
* GPT-4o-mini Integration
* Document Chunking Pipeline
* Local Vector Storage


## Technology Stack

### Backend

* Python 3.11
* FastAPI
* Uvicorn

### AI / Machine Learning

* OpenAI API
* GPT-4o-mini
* text-embedding-3-small

### Vector Database

* ChromaDB

### Libraries

* LangChain
* LangChain OpenAI
* Pydantic Settings

### Development

* Git
* GitHub
* VS Code


## Project Structure

RAG-Learning-Assistant/

├── app/

│   ├── api/

│   ├── config/

│   ├── embeddings/

│   ├── ingestion/

│   ├── llm/

│   ├── retrieval/

│   └── models/

│

├── scripts/

├── data/

├── main.py

├── requirements.txt

└── README.md


## Installation

Clone the repository:

git clone https://github.com/aramradif/RAG-Learning-Assistant.git

Navigate into the project:

cd RAG-Learning-Assistant

Create a virtual environment:

python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


## Running the API

Start FastAPI:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs


## Example Request

POST /ask

Request:

{
"question": "What is RAG?"
}

Response:

{
"answer": "RAG combines semantic search with large language models to provide grounded answers based on external documents."
}


## Roadmap

* Multi-document ingestion
* PDF support
* Conversational memory
* Hybrid search
* Evaluation framework
* Agentic workflows
* Multi-agent orchestration
* Cloud deployment
* Authentication & RBAC
* Production monitoring

# Enterprise Multi-Agent Policy Assistant

An enterprise Retrieval-Augmented Generation (RAG) application that answers employee policy questions using AI while ensuring responses are grounded in official company documentation.

This project demonstrates how modern enterprise AI assistants retrieve, validate, and confidently answer questions using OpenAI, LangChain, FAISS, and Streamlit.

---

## Features

- Semantic document search using OpenAI embeddings
- FAISS vector database
- Retrieval-Augmented Generation (RAG)
- AI-generated grounded responses
- AI response validation
- Confidence scoring
- Source document citation
- Interactive Streamlit web application

---

## Tech Stack

- Python
- OpenAI API
- LangChain
- FAISS
- Streamlit
- Recursive Text Splitter
- OpenAI Embeddings
- GPT-4.1-mini

---

## Project Architecture

User Question

↓

Streamlit Interface

↓

Document Retriever

↓

FAISS Vector Database

↓

Relevant Policy Chunks

↓

GPT-4.1-mini

↓

Validation Agent

↓

Confidence Scoring

↓

Grounded Response

---

## Project Structure

```
enterprise-multi-agent-policy-assistant/
│
├── documents/
├── src/
│ ├── document_loader.py
│ ├── text_splitter.py
│ ├── vector_store.py
│ ├── retriever.py
│ ├── response_agent.py
│ ├── validation_agent.py
│ ├── confidence.py
│ └── rag_pipeline.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Example Workflow

1. User submits a policy question.
2. Documents are searched using semantic similarity.
3. Relevant policy sections are retrieved.
4. GPT-4.1-mini generates an answer.
5. The Validation Agent verifies the response.
6. Confidence Score is calculated.
7. Sources are displayed.

---

## Sample Question

Can employees work remotely from another state?

The assistant retrieves the appropriate Remote Work Policy and generates a grounded response while displaying confidence and source references.

---

## Future Improvements

- Multi-document ranking
- Citation highlighting
- Conversation memory
- Multi-agent orchestration
- Azure OpenAI support
- Authentication and role-based access

---

## Author

Independent AI Portfolio Project

Built using Python, LangChain, OpenAI, FAISS, and Streamlit.
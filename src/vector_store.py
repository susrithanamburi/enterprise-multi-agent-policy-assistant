"""
vector_store.py

Creates and manages the vector database used for semantic search.
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks):
    """
    Build a FAISS vector database from document chunks.

    Args:
        chunks: List of LangChain Document chunks.

    Returns:
        FAISS vector database.
    """

    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    return vector_store
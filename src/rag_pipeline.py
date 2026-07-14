"""
rag_pipeline.py

Complete Enterprise RAG Pipeline.
"""

from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.response_agent import generate_response
from src.validation_agent import validate_response
from src.confidence import calculate_confidence


def run_pipeline(question: str):
    """
    Execute the complete RAG workflow.

    Args:
        question: User question.

    Returns:
        Dictionary containing response,
        validation status and confidence score.
    """

    # Step 1
    documents = load_documents()

    # Step 2
    chunks = split_documents(documents)

    # Step 3
    vector_store = create_vector_store(chunks)

    # Step 4
    retriever = create_retriever(vector_store)

    # Step 5
    retrieved_docs = retriever.invoke(question)

    # Step 6
    response = generate_response(
        question,
        retrieved_docs
    )

    # Step 7
    validation = validate_response(response)

    # Step 8
    confidence = calculate_confidence(retrieved_docs)

    return {
        "question": question,
        "response": response,
        "validation": validation,
        "confidence": confidence
    }
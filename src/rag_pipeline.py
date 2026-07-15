from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.response_agent import generate_response
from src.validation_agent import validate_response
from src.confidence import calculate_confidence


def run_pipeline(question: str):
    """
    Run the complete RAG workflow for one policy question.
    """

    documents = load_documents()
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)
    retriever = get_retriever(vector_store)

    retrieved_docs = retriever.invoke(question)

    response = generate_response(
        question,
        retrieved_docs
    )

    validation = validate_response(
        question,
        response,
        retrieved_docs
    )

    confidence = calculate_confidence(
        validation,
        retrieved_docs
    )

    sources = []

    for document in retrieved_docs:
        source = document.metadata.get("source", "Unknown source")

        if source not in sources:
            sources.append(source)

    return {
        "question": question,
        "response": response,
        "validation": validation,
        "confidence": confidence,
        "sources": sources
    }
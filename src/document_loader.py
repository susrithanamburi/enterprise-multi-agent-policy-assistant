"""
document_loader.py

Loads PDF documents from the documents folder
and prepares them for the RAG pipeline.
"""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(documents_path: str = "documents"):
    """
    Load all PDF documents from the specified folder.

    Args:
        documents_path: Folder containing PDF files.

    Returns:
        List of LangChain Document objects.
    """

    all_documents = []

    pdf_files = Path(documents_path).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()
        all_documents.extend(docs)

    return all_documents
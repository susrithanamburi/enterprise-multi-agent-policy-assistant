"""
text_splitter.py

Splits loaded policy documents into smaller overlapping chunks
for embedding generation and semantic retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(
    documents,
    chunk_size: int = 800,
    chunk_overlap: int = 120,
):
    """
    Split documents into smaller chunks while preserving metadata.

    Args:
        documents: LangChain Document objects produced by the document loader.
        chunk_size: Maximum number of characters in each chunk.
        chunk_overlap: Number of characters shared between neighboring chunks.

    Returns:
        List of smaller LangChain Document chunks.
    """

    if not documents:
        return []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
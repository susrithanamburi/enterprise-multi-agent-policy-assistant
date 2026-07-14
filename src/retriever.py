"""
retriever.py

Creates the semantic retriever that searches
the vector database for the most relevant chunks.
"""


def create_retriever(vector_store):
    """
    Convert the FAISS database into a retriever.

    Args:
        vector_store: FAISS vector database.

    Returns:
        LangChain Retriever.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )

    return retriever
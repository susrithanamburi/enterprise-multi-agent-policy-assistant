def get_retriever(vector_store):
    """
    Create a retriever for semantic search.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever
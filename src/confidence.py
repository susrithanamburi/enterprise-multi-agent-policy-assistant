"""
confidence.py

Simple confidence scoring based on retrieval results.
"""


def calculate_confidence(retrieved_docs):
    """
    Estimate confidence score.

    Args:
        retrieved_docs: Documents retrieved from FAISS.

    Returns:
        Confidence percentage.
    """

    if not retrieved_docs:
        return 0

    confidence = min(100, len(retrieved_docs) * 25)

    return confidence
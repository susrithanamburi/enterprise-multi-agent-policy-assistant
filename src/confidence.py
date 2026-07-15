def calculate_confidence(validation_result, retrieved_docs):
    """
    Calculate a simple confidence score based on
    validation results and retrieved evidence.
    """

    validation = validation_result.upper()

    if "PASS" in validation:
        score = min(70 + (len(retrieved_docs) * 10), 100)
    else:
        score = max(30 + (len(retrieved_docs) * 5), 40)

    return {
        "score": score,
        "status": "High" if score >= 90 else "Medium" if score >= 70 else "Low"
    }
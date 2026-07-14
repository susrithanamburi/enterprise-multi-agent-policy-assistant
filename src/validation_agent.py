"""
validation_agent.py

Performs basic validation of AI responses.
"""


def validate_response(response: str):
    """
    Validate the generated response.

    Args:
        response: AI-generated answer.

    Returns:
        Validation dictionary.
    """

    if not response:
        return {
            "valid": False,
            "reason": "Empty response."
        }

    if len(response.strip()) < 20:
        return {
            "valid": False,
            "reason": "Response too short."
        }

    return {
        "valid": True,
        "reason": "Validation passed."
    }
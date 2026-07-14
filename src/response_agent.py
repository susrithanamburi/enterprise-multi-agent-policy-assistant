"""
response_agent.py

Generates responses using the retrieved context.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def generate_response(question, retrieved_docs):
    """
    Generate an answer using the retrieved documents.

    Args:
        question: User question.
        retrieved_docs: Retrieved document chunks.

    Returns:
        AI-generated response.
    """

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an enterprise policy assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
say you do not have enough information.

Context:
{context}

Question:
{question}
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content
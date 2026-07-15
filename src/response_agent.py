from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_response(question, retrieved_docs):
    """
    Generate a grounded answer using the retrieved policy documents.
    """

    context = "\n\n".join(
        document.page_content for document in retrieved_docs
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are an enterprise policy assistant.

Answer the user's question using only the provided policy context.

Rules:
- Do not use outside knowledge.
- Do not invent details.
- If the answer is not available in the context, say:
  "I could not find enough information in the provided policies."
- Give a clear and concise answer.
- Mention the relevant policy source when available.
                """,
            ),
            (
                "human",
                """
Policy context:

{context}

User question:

{question}
                """,
            ),
        ]
    )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response.content
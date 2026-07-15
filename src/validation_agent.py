from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def validate_response(question, answer, retrieved_docs):
    """
    Validate whether the generated answer is supported
    by the retrieved policy documents.
    """

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are an AI quality reviewer.

Determine whether the answer is fully supported by the policy context.

Respond in this exact format:

Validation: PASS or FAIL

Reason:
<brief explanation>
                """
            ),
            (
                "human",
                """
Policy Context:

{context}

Question:

{question}

Answer:

{answer}
                """
            )
        ]
    )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    chain = prompt | llm

    result = chain.invoke(
        {
            "context": context,
            "question": question,
            "answer": answer
        }
    )

    return result.content
from app.llm.openai_client import client
from app.config.settings import settings
from app.retrieval.search import search_documents


def ask_rag(question: str) -> str:
    """
    Retrieve context and generate answer.
    """

    results = search_documents(question)

    context = "\n".join(results["documents"][0])

    prompt = f"""
Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content

def build_prompt(
    question: str,
    context: list[dict],
):
    """
    Build the prompt sent to the LLM.
    """

    context_text = "\n\n".join(item["content"] for item in context)

    prompt = f"""
You are an educational AI assistant.

Answer the user's question using ONLY the provided context.

Context:

{context_text}

Question:

{question}

Answer:
"""

    return prompt

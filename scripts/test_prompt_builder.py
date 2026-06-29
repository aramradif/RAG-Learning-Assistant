from app.llm.prompt_builder import build_prompt

context = [
    {"content": "Retrieval-Augmented Generation combines semantic search with LLMs."},
    {"content": "Source citations reduce hallucinations."},
]

prompt = build_prompt(
    question="What is RAG?",
    context=context,
)

print(prompt)

from app.services.rag_service import RAGService


service = RAGService()

prompt = service.build_prompt("What is RAG?")

print(prompt)

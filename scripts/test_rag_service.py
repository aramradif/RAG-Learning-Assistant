from app.services.rag_service import RAGService


service = RAGService()

results = service.retrieve("RAG")

for result in results:
    print(result["source"])

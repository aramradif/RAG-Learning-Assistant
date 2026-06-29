from app.llm.rag import ask_rag


question = "What is RAG?"

answer = ask_rag(question)

print("\nAnswer:\n")
print(answer)

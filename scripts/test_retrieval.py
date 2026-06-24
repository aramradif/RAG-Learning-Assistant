from app.retrieval.search import search_documents


query = "What is Retrieval-Augmented Generation?"

results = search_documents(query)

print("\nSearch Results:\n")

for doc in results["documents"][0]:
    print("-" * 50)
    print(doc)
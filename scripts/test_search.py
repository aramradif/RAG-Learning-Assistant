from app.retrieval.vector_store import collection


results = collection.get()

print("\nStored Documents:\n")

for i, doc in enumerate(results["documents"]):
    print(f"Document {i+1}")
    print("-" * 50)
    print(doc)
    print()
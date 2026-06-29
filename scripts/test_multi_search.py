from app.retrieval.search import search_documents

query = "academic integrity"

results = search_documents(query)

documents = results["documents"][0]
metadatas = results["metadatas"][0]

print("\nSearch Results:\n")

for document, metadata in zip(documents, metadatas):
    print(f"Source : {metadata['source']}")
    print(f"Chunk  : {metadata['chunk']}")
    print()
    print(document)
    print("\n----------------------------\n")

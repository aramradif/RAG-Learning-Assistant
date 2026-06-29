from app.retrieval.hybrid_search import hybrid_search


results = hybrid_search("RAG")

print()

for result in results:
    print("Source      :", result["source"])
    print("Chunk       :", result["chunk"])
    print("Retrieval   :", result["retrieval"])
    print()
    print(result["content"])
    print("-" * 40)

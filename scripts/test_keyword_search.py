from app.retrieval.keyword_search import keyword_search


results = keyword_search("RAG")

print(f"\nFound {len(results)} matching documents.\n")

for document in results:
    print(document["filename"])

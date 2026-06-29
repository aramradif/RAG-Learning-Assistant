from app.ingestion.folder_loader import load_documents


def keyword_search(query: str):

    documents = load_documents("data")

    matches = []

    query = query.lower()

    for document in documents:
        if query in document["content"].lower():
            matches.append(
                {
                    "content": document["content"],
                    "source": document["filename"],
                    "chunk": 0,
                    "retrieval": "keyword",
                }
            )

    return matches

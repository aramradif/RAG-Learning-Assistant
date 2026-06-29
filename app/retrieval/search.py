from app.embeddings.openai_embeddings import get_embedding
from app.retrieval.vector_store import collection


def search_documents(
    query: str,
    top_k: int = 3,
):
    """
    Semantic search using ChromaDB.
    """

    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )

    documents = []

    docs = results["documents"][0]
    metadata = results["metadatas"][0]

    for doc, meta in zip(docs, metadata):
        documents.append(
            {
                "content": doc,
                "source": meta["source"],
                "chunk": meta["chunk"],
                "retrieval": "semantic",
            }
        )

    return documents

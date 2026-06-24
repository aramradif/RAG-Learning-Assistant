from app.embeddings.openai_embeddings import get_embedding
from app.retrieval.vector_store import collection


def search_documents(
    query: str,
    top_k: int = 3,
):
    """
    Search for similar documents.
    """

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results
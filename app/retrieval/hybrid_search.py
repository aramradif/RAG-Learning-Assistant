from app.retrieval.search import search_documents
from app.retrieval.keyword_search import keyword_search


def hybrid_search(
    query: str,
    top_k: int = 3,
):

    semantic = search_documents(
        query,
        top_k=top_k,
    )

    keyword = keyword_search(query)

    merged = []

    seen = set()

    for result in semantic:
        if result["content"] not in seen:
            merged.append(result)

            seen.add(result["content"])

    for result in keyword:
        if result["content"] not in seen:
            merged.append(result)

            seen.add(result["content"])

    return merged

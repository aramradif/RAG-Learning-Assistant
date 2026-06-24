from app.embeddings.openai_embeddings import get_embedding
from app.retrieval.vector_store import collection


def index_chunks(chunks: list[str]):

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[f"chunk-{i}"],
            documents=[chunk],
            embeddings=[embedding],
        )

    print(f"Indexed {len(chunks)} chunks.")
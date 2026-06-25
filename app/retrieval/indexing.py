import uuid

from app.embeddings.openai_embeddings import get_embedding
from app.retrieval.vector_store import collection


def index_chunks(
    chunks: list[str],
    source: str,
):

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": source,
                    "chunk": i,
                }
            ],
        )

    print(f"Indexed {len(chunks)} chunks from {source}.")
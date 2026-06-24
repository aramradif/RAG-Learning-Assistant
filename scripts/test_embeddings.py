from app.embeddings.openai_embeddings import (
    get_embedding_model,
)

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "Artificial Intelligence"
)

print("Embedding Length:", len(vector))

print("\nFirst 10 Values:")

print(vector[:10])
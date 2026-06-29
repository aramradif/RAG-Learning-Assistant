from app.retrieval.vector_store import client

try:
    client.delete_collection("documents")
    print("Collection deleted.")
except Exception:
    print("Collection did not exist.")

client.create_collection("documents")

print("Fresh collection created.")

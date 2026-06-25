from app.ingestion.folder_loader import load_documents


documents = load_documents("data")

print(
    f"Loaded {len(documents)} documents."
)

for doc in documents:
    print(doc["filename"])
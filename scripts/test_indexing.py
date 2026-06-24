from app.ingestion.ingestion import load_text_document
from app.ingestion.chunking import chunk_text
from app.retrieval.indexing import index_chunks

document = load_text_document(
    "data/sample.txt"
)

chunks = chunk_text(document)

index_chunks(chunks)
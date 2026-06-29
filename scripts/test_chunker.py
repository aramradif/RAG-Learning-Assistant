from app.ingestion.ingestion import load_text_document
from app.ingestion.chunking import chunk_text


def main():
    text = load_text_document("data/sample.txt")

    chunks = chunk_text(
        text=text,
        chunk_size=50,
        overlap=10,
    )

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {i}")
        print("-" * 40)
        print(chunk)


if __name__ == "__main__":
    main()

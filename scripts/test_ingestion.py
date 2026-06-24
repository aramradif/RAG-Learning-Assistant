from app.ingestion.ingestion import load_text_document


def main():
    text = load_text_document("data/sample.txt")

    print("\nDocument Loaded Successfully\n")
    print(text)


if __name__ == "__main__":
    main()
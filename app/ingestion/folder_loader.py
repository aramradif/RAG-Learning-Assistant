from pathlib import Path


def load_documents(folder_path: str):
    """
    Load all text files from a folder.
    """

    documents = []

    for file_path in Path(folder_path).glob("*.txt"):

        text = file_path.read_text(
            encoding="utf-8"
        )

        documents.append(
            {
                "filename": file_path.name,
                "content": text,
            }
        )

    return documents
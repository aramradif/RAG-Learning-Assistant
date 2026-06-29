def select_context(
    documents: list[dict],
    max_documents: int = 3,
):
    """
    Select the most relevant documents
    to include in the prompt.
    """

    return documents[:max_documents]

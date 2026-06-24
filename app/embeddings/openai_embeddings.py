from langchain_openai import OpenAIEmbeddings

from app.config.settings import settings


def get_embedding_model():
    """
    Return OpenAI embedding model.
    """

    return OpenAIEmbeddings(
        api_key=settings.OPENAI_API_KEY,
        model=settings.EMBEDDING_MODEL,
    )


def get_embedding(text: str):
    """
    Generate embedding for text.
    """

    model = get_embedding_model()

    return model.embed_query(text)
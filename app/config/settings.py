from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "RAG Learning Assistant API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Production-ready Retrieval-Augmented Generation API"

    OPENAI_API_KEY: str = ""

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    LLM_MODEL: str = "gpt-4o-mini"

    VECTOR_DB_PATH: str = "./data/vector_store"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    class Config:
        env_file = ".env"


settings = Settings()

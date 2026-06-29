from app.config.settings import settings

print("API Key Loaded:", settings.OPENAI_API_KEY[:10] + "...")
print("Embedding Model:", settings.EMBEDDING_MODEL)

import chromadb

from app.config.settings import settings

client = chromadb.PersistentClient(path=settings.VECTOR_DB_PATH)

collection = client.get_or_create_collection(name="documents")

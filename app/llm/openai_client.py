from openai import OpenAI

from app.config.settings import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)

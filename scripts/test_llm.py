from openai import OpenAI

from app.config.settings import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)

response = client.chat.completions.create(
    model=settings.LLM_MODEL,
    messages=[{"role": "user", "content": "What is Retrieval-Augmented Generation?"}],
)

print(response.choices[0].message.content)

"""OpenAI Embedding API로 텍스트를 벡터로 바꾸는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 Embedding API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

text = "FastAPI는 Python으로 API 서버를 만들 때 사용하는 웹 프레임워크입니다."
response = client.embeddings.create(model=embedding_model, input=text)
embedding = response.data[0].embedding

print("embedding dimension:", len(embedding))
print("first 10 values:", embedding[:10])

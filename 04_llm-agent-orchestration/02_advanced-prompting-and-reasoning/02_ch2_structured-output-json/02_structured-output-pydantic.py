"""Pydantic 모델로 Structured Output을 받는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


class LearningFeedback(BaseModel):
    """LLM 응답이 따라야 할 구조를 코드로 정의합니다."""

    summary: str = Field(description="학습 피드백 한 문장 요약")
    sentiment: str = Field(description="positive, neutral, negative 중 하나")
    keywords: list[str] = Field(description="핵심 키워드 목록")
    difficulty: int = Field(description="학습 난이도. 1부터 5까지")


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

# parse는 지정한 Pydantic 구조에 맞는 응답을 받는 데 사용합니다.
response = client.responses.parse(
    model=model,
    input="오늘 FastAPI 실습은 어렵지만 재미있었고, Docker는 아직 헷갈린다.",
    text_format=LearningFeedback,
)

feedback = response.output_parsed
print(feedback)
print("\n요약:", feedback.summary)
print("키워드:", ", ".join(feedback.keywords))

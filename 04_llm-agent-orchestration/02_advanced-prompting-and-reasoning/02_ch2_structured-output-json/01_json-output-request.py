"""프롬프트로 JSON 형식 응답을 요청하는 예제입니다."""

from pathlib import Path
import json
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    raise SystemExit(0)

client = OpenAI()

prompt = """
아래 문장을 분석해서 JSON으로만 답해라.

문장: 오늘 FastAPI 실습은 어렵지만 재미있었고, Docker는 아직 헷갈린다.

JSON 형식:
{
  "summary": "한 문장 요약",
  "sentiment": "positive | neutral | negative",
  "keywords": ["키워드1", "키워드2"],
  "difficulty": 1
}
""".strip()

response = client.responses.create(model=model, input=prompt)
text = response.output_text
print(text)

# 모델이 JSON 형식을 지켰는지 Python에서 확인합니다.
try:
    parsed = json.loads(text)
except json.JSONDecodeError:
    print("\nJSON 파싱에 실패했습니다. Structured Output이 필요한 이유를 확인하세요.")
else:
    print("\nJSON 파싱 성공")
    print(parsed)

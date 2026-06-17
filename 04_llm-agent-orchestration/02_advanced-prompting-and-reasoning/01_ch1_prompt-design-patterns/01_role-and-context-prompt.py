"""역할, 맥락, 작업, 출력 형식을 나누어 프롬프트를 작성하는 예제입니다."""

from pathlib import Path
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

# 역할, 맥락, 작업, 출력 형식을 분리하면 모델이 요청을 더 안정적으로 이해합니다.
prompt = """
# 역할
너는 Python과 FastAPI를 가르치는 강사다.

# 맥락
수강생은 Python 기초를 막 끝냈고 FastAPI를 처음 배운다.

# 작업
FastAPI의 핵심 개념을 초보자에게 설명해라.

# 출력 형식
- 핵심 요약 3줄
- 쉬운 비유 1개
- 다음에 공부할 키워드 3개
""".strip()

response = client.responses.create(model=model, input=prompt)
print(response.output_text)

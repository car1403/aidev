"""예시를 제공해서 원하는 답변 스타일을 유도하는 예제입니다."""

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

# 예시를 함께 주면 모델이 원하는 답변 톤과 형식을 따라가기 쉽습니다.
prompt = """
너는 개발 입문자를 위한 용어 설명 도우미다.
아래 예시처럼 짧고 쉽게 설명해라.

예시 입력: 변수
예시 출력:
개념: 값을 담아두는 이름이다.
비유: 이름표가 붙은 상자와 비슷하다.
예시: age = 20

실제 입력: API
""".strip()

response = client.responses.create(model=model, input=prompt)
print(response.output_text)

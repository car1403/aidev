"""역할을 나누어 LLM에게 요청하는 예제입니다."""

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

# system 역할은 모델의 행동 기준을 정합니다.
# user 역할은 사용자의 실제 요청을 전달합니다.
response = client.responses.create(
    model=model,
    input=[
        {
            "role": "system",
            "content": "너는 Python 입문자를 가르치는 친절한 강사다. 답변은 쉽고 짧게 작성한다.",
        },
        {
            "role": "user",
            "content": "환경 변수를 사용하는 이유를 예시와 함께 설명해줘.",
        },
    ],
)

print(response.output_text)

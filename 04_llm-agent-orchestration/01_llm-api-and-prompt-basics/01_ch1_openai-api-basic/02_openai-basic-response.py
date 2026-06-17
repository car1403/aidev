"""OpenAI Responses API로 첫 응답을 받아보는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# .env 파일을 읽어 API Key와 모델명을 환경 변수로 등록합니다.
BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# API Key가 없으면 실제 호출을 하지 않고 종료합니다.
if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 설정되지 않아 API 호출을 건너뜁니다.")
    raise SystemExit(0)

# OpenAI SDK는 OPENAI_API_KEY 환경 변수를 자동으로 사용합니다.
client = OpenAI()

# input에는 모델에게 전달할 사용자 요청을 작성합니다.
response = client.responses.create(
    model=model,
    input="Python을 처음 배우는 사람에게 API가 무엇인지 세 문장으로 설명해줘.",
)

# output_text에는 모델이 생성한 최종 텍스트가 들어 있습니다.
print(response.output_text)

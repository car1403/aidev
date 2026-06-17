"""OpenAI API Key 환경 변수를 확인하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv


# 현재 파일 위치를 기준으로 상위 폴더의 .env 파일 경로를 계산합니다.
BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

# .env 파일이 있으면 환경 변수로 읽어옵니다.
load_dotenv(ENV_PATH)

# OpenAI API Key는 실제 값을 출력하지 않고 존재 여부만 확인합니다.
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key or api_key == "your-openai-api-key":
    print("OPENAI_API_KEY가 아직 설정되지 않았습니다.")
    print(".env.example 파일을 복사해서 .env 파일을 만든 뒤 실제 API Key를 입력하세요.")
else:
    print("OPENAI_API_KEY가 설정되어 있습니다.")
    print(f"사용할 모델: {model}")

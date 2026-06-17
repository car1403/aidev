"""LangSmith tracing 환경 변수 설정 상태를 확인하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

tracing = os.getenv("LANGSMITH_TRACING", "false")
api_key = os.getenv("LANGSMITH_API_KEY", "")
project = os.getenv("LANGSMITH_PROJECT", "aidev-langgraph-practice")

print("LANGSMITH_TRACING:", tracing)
print("LANGSMITH_PROJECT:", project)

if tracing.lower() == "true" and api_key and api_key != "your-langsmith-api-key":
    print("LangSmith tracing을 사용할 준비가 되어 있습니다.")
elif tracing.lower() == "true":
    print("LANGSMITH_TRACING은 true이지만 API Key가 설정되지 않았습니다.")
else:
    print("LangSmith tracing은 비활성화되어 있습니다. 기본 실습에는 문제가 없습니다.")

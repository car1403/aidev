"""Ollama REST API로 로컬 Llama 모델을 호출하는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
model = os.getenv("OLLAMA_MODEL", "llama3.2")

payload = {
    "model": model,
    "prompt": "Python을 처음 배우는 사람에게 함수가 무엇인지 두 문장으로 설명해줘.",
    "stream": False,
}

try:
    # /api/generate는 Ollama의 기본 텍스트 생성 API입니다.
    response = httpx.post(f"{base_url}/api/generate", json=payload, timeout=120.0)
    response.raise_for_status()
except httpx.HTTPError as exc:
    print("Llama 모델 호출에 실패했습니다.")
    print("Ollama 컨테이너 실행 여부와 모델 다운로드 여부를 확인하세요.")
    print(f"오류 내용: {exc}")
else:
    data = response.json()
    print(data.get("response", "응답 텍스트를 찾지 못했습니다."))

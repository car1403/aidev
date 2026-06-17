"""Ollama 서버가 실행 중인지 확인하는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

try:
    # Ollama 서버의 태그 목록 API를 호출해서 서버 상태를 확인합니다.
    response = httpx.get(f"{base_url}/api/tags", timeout=5.0)
    response.raise_for_status()
except httpx.HTTPError as exc:
    print("Ollama 서버에 연결하지 못했습니다.")
    print("먼저 Docker Desktop을 실행한 뒤 docker run 명령으로 ollama-llm 컨테이너를 실행하세요.")
    print(f"오류 내용: {exc}")
else:
    print("Ollama 서버가 실행 중입니다.")
    print("현재 다운로드된 모델 목록:")
    print(response.json())

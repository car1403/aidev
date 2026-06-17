"""OpenAI와 로컬 Llama에 같은 질문을 보내 비교하는 예제입니다."""

from pathlib import Path
import os
import time

import httpx
from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
PROMPT = "FastAPI가 무엇인지 Python 초보자에게 세 문장으로 설명해줘."


def call_openai(prompt: str) -> tuple[str, float]:
    """OpenAI API를 호출하고 응답 텍스트와 소요 시간을 반환합니다."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-openai-api-key":
        return "OPENAI_API_KEY가 설정되지 않아 호출하지 않았습니다.", 0.0

    client = OpenAI()
    started_at = time.perf_counter()
    response = client.responses.create(model=OPENAI_MODEL, input=prompt)
    elapsed = time.perf_counter() - started_at
    return response.output_text, elapsed


def call_ollama(prompt: str) -> tuple[str, float]:
    """Ollama API를 호출하고 응답 텍스트와 소요 시간을 반환합니다."""
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    started_at = time.perf_counter()
    try:
        response = httpx.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=120.0)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        return f"Ollama 호출에 실패했습니다: {exc}", 0.0

    elapsed = time.perf_counter() - started_at
    return response.json().get("response", "응답 텍스트를 찾지 못했습니다."), elapsed


openai_text, openai_elapsed = call_openai(PROMPT)
ollama_text, ollama_elapsed = call_ollama(PROMPT)

print("[질문]")
print(PROMPT)
print("\n[OpenAI 응답]")
print(openai_text)
print(f"소요 시간: {openai_elapsed:.2f}초")
print("\n[Llama 응답]")
print(ollama_text)
print(f"소요 시간: {ollama_elapsed:.2f}초")

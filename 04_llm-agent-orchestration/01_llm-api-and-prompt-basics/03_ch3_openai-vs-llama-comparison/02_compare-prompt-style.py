"""출력 형식을 지정했을 때 OpenAI와 Llama 응답을 비교하는 예제입니다."""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

PROMPT = """
Python 리스트를 초보자에게 설명해줘.
반드시 아래 형식으로만 답변해줘.

개념: 한 문장
예시: 짧은 코드 한 줄
주의점: 한 문장
""".strip()


def call_openai(prompt: str) -> str:
    """OpenAI API에 형식 고정 프롬프트를 보냅니다."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-openai-api-key":
        return "OPENAI_API_KEY가 설정되지 않아 호출하지 않았습니다."

    client = OpenAI()
    response = client.responses.create(model=OPENAI_MODEL, input=prompt)
    return response.output_text


def call_ollama(prompt: str) -> str:
    """Ollama API에 형식 고정 프롬프트를 보냅니다."""
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    try:
        response = httpx.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=120.0)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        return f"Ollama 호출에 실패했습니다: {exc}"

    return response.json().get("response", "응답 텍스트를 찾지 못했습니다.")


print("[프롬프트]")
print(PROMPT)
print("\n[OpenAI 응답]")
print(call_openai(PROMPT))
print("\n[Llama 응답]")
print(call_ollama(PROMPT))

r"""Gemini REST 싱글턴 호출 예제입니다.

주의:
    이 파일은 GEMINI_API_KEY가 설정되어 있을 때 실제 API를 호출합니다.
    실제 사용 조건과 무료 범위는 수업 시점의 공식 화면에서 확인합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\03_single-turn-call\03_gemini_rest_single_turn.py
"""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


# 이 예제는 SDK 대신 REST API를 직접 호출합니다.
# 따라서 URL, query parameter, JSON payload 구조를 직접 확인할 수 있습니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 API key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not is_real_api_key(api_key):
        # key가 없으면 실제 외부 API를 호출하지 않습니다.
        print("GEMINI_API_KEY가 없거나 placeholder 값입니다. 먼저 mock 예제로 학습하세요.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    # Gemini REST API는 key를 query parameter로 전달하는 형태를 사용할 수 있습니다.
    params = {"key": api_key}
    # payload는 HTTP 요청 본문입니다.
    # contents에는 사용자의 질문을 넣고, generationConfig에는 생성 옵션을 넣습니다.
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "참고 메모: Pydantic은 요청 데이터를 검증하고 잘못된 요청을 422 오류로 처리한다.\n"
                            "질문: FastAPI에서 Pydantic을 왜 사용하나요? 초보자에게 설명해 주세요."
                        )
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 300,
        },
    }

    # timeout은 외부 API가 오래 응답하지 않을 때 무한 대기하지 않도록 막아줍니다.
    response = httpx.post(url, params=params, json=payload, timeout=30)
    # 4xx/5xx 응답이면 예외를 발생시켜 문제를 빨리 확인합니다.
    response.raise_for_status()
    data = response.json()

    # REST 응답 JSON에서 실제 답변 텍스트가 들어 있는 위치를 꺼냅니다.
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print(text)


if __name__ == "__main__":
    main()

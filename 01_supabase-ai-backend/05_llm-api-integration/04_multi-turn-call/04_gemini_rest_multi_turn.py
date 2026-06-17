"""Gemini REST 멀티턴 호출 예제.

01~03 과정에서는 Gemini API를 기본 LLM 실습 모델로 사용합니다.
이 파일은 GEMINI_API_KEY가 설정되어 있을 때만 실제 API를 호출합니다.

멀티턴 호출은 모델이 대화를 자동으로 기억한다는 뜻이 아닙니다.
이전 user/assistant 메시지를 코드에서 다시 payload에 넣어 보내기 때문에
모델이 앞 대화의 맥락을 참고할 수 있습니다.
"""

from pathlib import Path
import os

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def main() -> None:
    """Gemini REST API로 이전 대화가 포함된 질문을 보냅니다."""

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not api_key:
        print("GEMINI_API_KEY가 없습니다. 먼저 mock 멀티턴 예제로 학습하세요.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    params = {"key": api_key}

    # Gemini REST API의 contents 목록에 이전 대화를 순서대로 넣습니다.
    # role은 user 또는 model을 사용합니다.
    # OpenAI 예제의 assistant 역할은 Gemini에서는 model 역할에 가깝게 표현합니다.
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": "FastAPI가 무엇인가요?"}],
            },
            {
                "role": "model",
                "parts": [{"text": "Python으로 API 서버를 쉽게 만들 수 있는 프레임워크입니다."}],
            },
            {
                "role": "user",
                "parts": [{"text": "그 설명을 바탕으로 Pydantic의 역할을 초보자에게 설명해 주세요."}],
            },
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 400,
        },
    }

    response = httpx.post(url, params=params, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print(text)


if __name__ == "__main__":
    main()

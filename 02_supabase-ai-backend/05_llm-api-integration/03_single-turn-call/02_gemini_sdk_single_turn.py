r"""Gemini SDK 기반 싱글턴 호출 예제입니다.

이 파일은 Google Gen AI SDK를 사용해 Gemini API를 호출합니다.

현재 폴더의 호출 흐름:
    01_mock_single_turn.py
        실제 API를 호출하지 않고 싱글턴 구조를 먼저 이해합니다.

    02_gemini_sdk_single_turn.py
        Gemini SDK로 가장 짧고 읽기 쉬운 실제 호출을 연습합니다.

    03_gemini_rest_single_turn.py
        REST API를 직접 호출하며 HTTP URL, payload, 응답 JSON 구조를 이해합니다.

    04_openai_single_turn.py
        OpenAI API를 선택/비교 실습으로 확인합니다.

주의:
    이 파일은 GEMINI_API_KEY가 실제 key로 설정되어 있을 때만 API를 호출합니다.
    key가 없거나 placeholder 값이면 실제 API를 호출하지 않고 안내 메시지를 출력합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\03_single-turn-call\02_gemini_sdk_single_turn.py
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# .env 파일은 02_supabase-ai-backend 폴더에 있으므로 두 단계 위로 이동합니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아닌 실제 API key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not is_real_api_key(api_key):
        print("GEMINI_API_KEY가 없거나 placeholder 값입니다.")
        print("먼저 01_mock_single_turn.py로 구조를 이해한 뒤, .env에 실제 Gemini API key를 설정하세요.")
        return

    try:
        from google import genai
    except ModuleNotFoundError:
        print("google-genai 패키지가 설치되어 있지 않습니다.")
        print("다음 명령으로 requirements.txt의 패키지를 먼저 설치하세요.")
        print(r"pip install -r requirements.txt")
        return

    # SDK 방식은 REST 방식보다 코드가 짧습니다.
    # URL, query parameter, JSON payload를 직접 만들지 않아도 됩니다.
    client = genai.Client(api_key=api_key)

    prompt = (
        "참고 메모: Pydantic은 요청 데이터를 검증하고 잘못된 요청을 422 오류로 처리한다.\n"
        "질문: FastAPI에서 Pydantic을 왜 사용하나요? 초보자에게 설명해 주세요."
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "temperature": 0.2,
            "max_output_tokens": 300,
        },
    )

    # SDK는 응답 텍스트를 response.text로 쉽게 꺼낼 수 있습니다.
    print(response.text)


if __name__ == "__main__":
    main()

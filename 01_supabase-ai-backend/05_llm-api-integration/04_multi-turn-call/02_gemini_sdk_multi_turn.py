r"""Gemini SDK 기반 멀티턴 호출 예제입니다.

이 파일은 04_multi-turn-call 단원의 중심 예제입니다.

멀티턴 호출의 핵심:
    모델이 이전 대화를 자동으로 기억하는 것이 아닙니다.
    코드에서 이전 user/model 메시지를 다시 함께 보내기 때문에
    모델이 앞 대화의 맥락을 참고할 수 있습니다.

현재 폴더의 호출 흐름:
    00_conversation-memory-concept.py
        대화 이력을 코드에서 어떻게 관리하는지 먼저 확인합니다.

    01_mock_multi_turn.py
        실제 API 호출 없이 멀티턴 구조를 확인합니다.

    02_gemini_sdk_multi_turn.py
        실제 프로젝트에서 기본으로 사용할 Gemini SDK 멀티턴 호출입니다.

    03_gemini_rest_multi_turn.py
        HTTP URL, payload, JSON 응답 구조를 직접 확인하는 보충 예제입니다.

    04_openai_multi_turn.py
        OpenAI API 선택/비교 예제입니다.

실행:
    cd C:\aidev\01_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\04_multi-turn-call\02_gemini_sdk_multi_turn.py
"""

from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 API key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def build_gemini_contents() -> list[dict[str, object]]:
    """Gemini SDK에 전달할 멀티턴 대화 이력을 만듭니다.

    Gemini에서는 AI가 이전에 답한 메시지를 `model` 역할로 표현합니다.
    OpenAI의 `assistant` 역할과 비슷하다고 생각하면 됩니다.
    """

    return [
        {
            "role": "user",
            "parts": [{"text": "FastAPI에서 Pydantic을 왜 사용하나요?"}],
        },
        {
            "role": "model",
            "parts": [{"text": "요청 데이터를 검증하고 응답 모델을 정리하는 데 사용합니다."}],
        },
        {
            "role": "user",
            "parts": [{"text": "그럼 메모 API에서는 어떤 부분에 도움이 되나요? 초보자에게 설명해 주세요."}],
        },
    ]


def main() -> None:
    """Gemini SDK로 이전 대화가 포함된 질문을 보냅니다."""

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

    if not is_real_api_key(api_key):
        print("GEMINI_API_KEY가 없거나 placeholder 값입니다.")
        print("먼저 01_mock_multi_turn.py로 멀티턴 구조를 이해한 뒤 실제 key를 설정하세요.")
        return

    try:
        from google import genai
    except ModuleNotFoundError:
        print("google-genai 패키지가 설치되어 있지 않습니다.")
        print("다음 명령으로 requirements.txt의 패키지를 먼저 설치하세요.")
        print(r"pip install -r requirements.txt")
        return

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=build_gemini_contents(),
        config={
            "temperature": 0.3,
            "max_output_tokens": 400,
        },
    )

    print(response.text)


if __name__ == "__main__":
    main()

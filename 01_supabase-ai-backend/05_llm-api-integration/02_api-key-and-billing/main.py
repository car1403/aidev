r"""LLM API key와 비용 안전 체크를 비용 없이 확인하는 통합 예제입니다.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
.env 파일에 key가 있는지, 기본 모델명이 무엇인지, 실제 호출 전에 무엇을 확인해야 하는지
안전 체크리스트 형태로 출력합니다.

실행:
    cd C:\aidev\01_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\02_api-key-and-billing\main.py
"""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(ENV_PATH)


@dataclass
class ProviderStatus:
    """LLM provider별 설정 상태를 저장합니다."""

    provider: str
    model: str
    has_api_key: bool
    api_key_name: str
    role_in_course: str


def mask_secret(value: str | None) -> str:
    """API key를 직접 출력하지 않고 일부만 가려서 보여줍니다."""

    if not is_real_api_key(value):
        return "없음"
    if len(value) <= 8:
        return "설정됨"
    return f"{value[:4]}...{value[-4:]}"


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제로 입력된 key인지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def load_provider_status() -> list[ProviderStatus]:
    """Gemini와 OpenAI 설정 상태를 읽습니다."""

    return [
        ProviderStatus(
            provider="gemini",
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite"),
            has_api_key=is_real_api_key(os.getenv("GEMINI_API_KEY")),
            api_key_name="GEMINI_API_KEY",
            role_in_course="01~03 과정의 기본 LLM 실습 provider",
        ),
        ProviderStatus(
            provider="openai",
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            has_api_key=is_real_api_key(os.getenv("OPENAI_API_KEY")),
            api_key_name="OPENAI_API_KEY",
            role_in_course="선택/비교 실습 provider",
        ),
    ]


def print_env_status() -> None:
    """환경변수 설정 상태를 출력합니다."""

    print("1. .env 설정 상태")
    print("-" * 50)
    print(f".env path: {ENV_PATH}")
    print(f"GEMINI_API_KEY: {mask_secret(os.getenv('GEMINI_API_KEY'))}")
    print(f"GEMINI_MODEL: {os.getenv('GEMINI_MODEL', 'gemini-2.5-flash-lite')}")
    print(f"OPENAI_API_KEY: {mask_secret(os.getenv('OPENAI_API_KEY'))}")
    print(f"OPENAI_MODEL: {os.getenv('OPENAI_MODEL', 'gpt-4.1-mini')}")
    print()


def print_provider_status() -> None:
    """provider별 수업 역할과 key 설정 여부를 출력합니다."""

    print("2. Provider별 사용 기준")
    print("-" * 50)

    for status in load_provider_status():
        print(f"provider: {status.provider}")
        print(f"model: {status.model}")
        print(f"api key name: {status.api_key_name}")
        print(f"key configured: {status.has_api_key}")
        print(f"course role: {status.role_in_course}")
        print()


def print_safety_checklist() -> None:
    """실제 API 호출 전에 확인할 안전 체크리스트를 출력합니다."""

    print("3. 실제 API 호출 전 안전 체크리스트")
    print("-" * 50)

    checklist = [
        "API key를 코드에 직접 적지 않았는가?",
        ".env 파일이 .gitignore에 포함되어 있는가?",
        "화면 공유나 녹화에서 API key가 보이지 않는가?",
        "공식 가격/무료 범위/호출 제한 페이지를 확인했는가?",
        "반복문 안에서 실제 API를 무제한 호출하지 않는가?",
        "max_tokens 또는 maxOutputTokens를 너무 크게 잡지 않았는가?",
        "실패 시 재시도 횟수를 제한했는가?",
        "OpenAI API 결제와 ChatGPT/Codex 앱 결제가 별개임을 이해했는가?",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")

    print()


def print_next_steps() -> None:
    """다음 학습 단계 안내를 출력합니다."""

    print("4. 다음 단계")
    print("-" * 50)

    if is_real_api_key(os.getenv("GEMINI_API_KEY")):
        print("GEMINI_API_KEY가 설정되어 있습니다.")
        print("다음 단원에서 Gemini 싱글턴 호출 예제를 실행할 수 있습니다.")
    else:
        print("GEMINI_API_KEY가 아직 없습니다.")
        print("다음 단원에서도 먼저 mock 예제로 구조를 확인한 뒤 key를 설정해도 됩니다.")

    if is_real_api_key(os.getenv("OPENAI_API_KEY")):
        print("OPENAI_API_KEY도 설정되어 있습니다.")
        print("OpenAI 예제는 선택/비교 실습에서 사용할 수 있습니다.")
    else:
        print("OPENAI_API_KEY는 없어도 됩니다. OpenAI 예제는 선택/비교 실습입니다.")


def main() -> None:
    """환경 설정과 비용 안전 체크를 순서대로 출력합니다."""

    print_env_status()
    print_provider_status()
    print_safety_checklist()
    print_next_steps()


if __name__ == "__main__":
    main()

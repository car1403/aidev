r"""LLM 설정을 안전하게 읽는 예제입니다.

실제 API key를 print하지 않고, 코드에서 사용할 설정 객체만 만듭니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\02_api-key-and-billing\02_safe_config_loader.py
"""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass
class LlmConfig:
    # provider는 gemini, openai처럼 어떤 LLM 서비스를 사용할지 나타냅니다.
    # 01~03 과정에서는 gemini를 기본 provider로 사용합니다.
    provider: str
    # model은 실제로 호출할 모델 이름입니다. .env에서 바꿀 수 있게 분리합니다.
    model: str
    # has_api_key는 key 자체가 아니라 "설정 여부"만 저장합니다.
    # 이렇게 하면 로그에 민감 정보가 노출되는 실수를 줄일 수 있습니다.
    has_api_key: bool
    # required는 이 과정에서 필수인지 선택인지 구분하기 위한 값입니다.
    required: bool


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 key가 들어왔는지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


def load_llm_config(provider: str) -> LlmConfig:
    """provider 이름에 따라 필요한 환경변수를 읽습니다."""

    if provider == "openai":
        # os.getenv의 두 번째 인자는 기본값입니다.
        # .env에 OPENAI_MODEL이 없으면 기본 모델명을 사용합니다.
        return LlmConfig(
            provider="openai",
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            has_api_key=is_real_api_key(os.getenv("OPENAI_API_KEY")),
            required=False,
        )

    if provider == "gemini":
        # Gemini도 동일한 구조로 읽습니다.
        # provider별 설정을 함수 하나에서 관리하면 FastAPI endpoint에서 재사용하기 쉽습니다.
        return LlmConfig(
            provider="gemini",
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite"),
            has_api_key=is_real_api_key(os.getenv("GEMINI_API_KEY")),
            required=True,
        )

    raise ValueError("provider는 openai 또는 gemini만 사용할 수 있습니다.")


for provider_name in ["gemini", "openai"]:
    # 실제 key를 출력하지 않고 설정 상태만 확인합니다.
    config = load_llm_config(provider_name)
    print(config)

print("\n핵심:")
print("Gemini는 01~03 과정의 기본 실습 provider입니다.")
print("OpenAI는 선택/비교 실습 provider이므로 key가 없어도 초반 과정은 진행할 수 있습니다.")

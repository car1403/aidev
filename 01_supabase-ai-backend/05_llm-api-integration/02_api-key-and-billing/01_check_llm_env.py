r"""LLM API 환경변수 확인 예제입니다.

이 파일은 실제 API를 호출하지 않습니다.
.env에 Gemini 또는 OpenAI key가 있는지 여부만 확인합니다.
01~03 과정에서는 Gemini API를 기본으로 사용하고, OpenAI API는 선택/비교 실습용으로 둡니다.

실행:
    cd C:\aidev\01_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# 이 파일은 05_llm-api-integration/02_api-key-and-billing 안에 있습니다.
# parents[2]를 사용하면 01_supabase-ai-backend 폴더로 올라갑니다.
# 즉, 과정 전체에서 공통으로 사용하는 .env 파일을 읽을 수 있습니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"

# load_dotenv는 .env 파일에 적은 값을 os.getenv로 읽을 수 있게 등록합니다.
load_dotenv(ENV_PATH)


def mask_secret(value: str | None) -> str:
    """secret 값을 직접 출력하지 않기 위해 일부만 보여줍니다."""

    if not is_real_api_key(value):
        return "없음"
    if len(value) <= 8:
        return "설정됨"
    return f"{value[:4]}...{value[-4:]}"


def is_real_api_key(value: str | None) -> bool:
    """placeholder가 아니라 실제 key가 들어왔는지 확인합니다."""

    if not value:
        return False

    normalized = value.strip().lower()
    placeholder_words = ["your-", "your_", "api-key", "apikey", "example", "sample", "placeholder"]

    return not any(word in normalized for word in placeholder_words)


gemini_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
openai_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


print("LLM API 환경변수 확인")
print("-" * 50)
print(f".env path: {ENV_PATH}")
print(f"GEMINI_API_KEY: {mask_secret(gemini_key)}")
print(f"GEMINI_MODEL: {gemini_model}")
print(f"OPENAI_API_KEY: {mask_secret(openai_key)}")
print(f"OPENAI_MODEL: {openai_model}")

if not is_real_api_key(gemini_key):
    # key가 없어도 수업은 진행할 수 있습니다.
    # 먼저 mock 예제로 요청/응답 구조를 익힌 뒤 실제 API 호출로 넘어갑니다.
    print("\nGEMINI_API_KEY가 아직 없습니다.")
    print("01~03 과정의 실제 LLM 호출은 Gemini API를 기본으로 진행합니다.")
    print("이 상태에서는 mock 예제로 먼저 학습하면 됩니다.")
else:
    # key가 있다는 것은 실제 호출이 가능하다는 뜻입니다.
    # 실제 호출 전에는 반드시 과금 상태, 호출 횟수, max_tokens 값을 확인합니다.
    print("\nGEMINI_API_KEY가 설정되어 있습니다.")
    print("실제 호출 전 공식 가격, 무료 범위, 호출 제한, maxOutputTokens 값을 확인하세요.")

if is_real_api_key(openai_key):
    print("\nOPENAI_API_KEY도 설정되어 있습니다.")
    print("OpenAI 예제는 선택/비교 실습으로 사용할 수 있습니다.")
else:
    print("\nOPENAI_API_KEY는 설정하지 않아도 됩니다.")
    print("OpenAI API는 선택/비교 실습에서만 사용합니다.")

print("\n주의:")
print("ChatGPT/Codex 앱 결제와 OpenAI API 결제는 별개로 확인해야 합니다.")
print("API key는 코드, README, GitHub에 직접 올리지 않습니다.")

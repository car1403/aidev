from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


# 이 파일은 다음 위치에 있습니다.
# 02_supabase-ai-backend/06_supabase-db-and-auth/01_supabase-project-and-env/01_check_supabase_env.py
# parents[2]는 02_supabase-ai-backend 폴더입니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


PLACEHOLDER_PREFIXES = (
    "your-",
    "https://your-",
)


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다.

    .env.example에는 your-supabase-anon-key 같은 샘플 값이 들어 있습니다.
    이런 값은 실제 Supabase key가 아니므로 "설정 완료"로 보면 안 됩니다.
    """

    if value is None:
        return False

    cleaned = value.strip()
    return any(cleaned.startswith(prefix) for prefix in PLACEHOLDER_PREFIXES)


def mask_secret(value: str | None) -> str:
    """환경 변수 값을 안전하게 출력합니다.

    API key와 service role key는 비밀번호처럼 다루어야 합니다.
    따라서 전체 값을 print하지 않고 앞뒤 일부만 보여줍니다.
    """

    if not value:
        return "(not set)"

    cleaned = value.strip()
    if is_placeholder(cleaned):
        return "(placeholder value)"

    if len(cleaned) <= 12:
        return "(set, but too short to verify safely)"

    return f"{cleaned[:6]}...{cleaned[-4:]}"


def read_env_value(name: str) -> str | None:
    """환경 변수 값을 읽고, 빈 문자열이면 None처럼 처리합니다."""

    value = os.getenv(name)
    if value is None:
        return None

    cleaned = value.strip()
    return cleaned or None


def print_env_status(name: str, value: str | None, secret: bool = True) -> bool:
    """환경 변수 하나의 상태를 출력하고, 실제 값인지 여부를 반환합니다."""

    if not value:
        print(f"- {name}: missing")
        return False

    if is_placeholder(value):
        print(f"- {name}: placeholder value")
        return False

    if secret:
        print(f"- {name}: {mask_secret(value)}")
    else:
        print(f"- {name}: {value}")

    return True


def main() -> None:
    """Supabase 실습에 필요한 환경 변수 설정 상태를 확인합니다."""

    # load_dotenv는 지정한 .env 파일의 값을 현재 Python 프로그램 환경 변수로 읽어 옵니다.
    # override=False가 기본값이므로, 이미 운영체제 환경 변수에 값이 있으면 덮어쓰지 않습니다.
    load_dotenv(ENV_PATH)

    supabase_url = read_env_value("SUPABASE_URL")
    anon_key = read_env_value("SUPABASE_ANON_KEY")
    service_role_key = read_env_value("SUPABASE_SERVICE_ROLE_KEY")

    print("[Supabase environment check]")
    print(f".env path: {ENV_PATH}")

    # URL은 key가 아니므로 전체를 출력해도 됩니다.
    # 다만 your-project-ref 같은 예시 값이면 실제 설정으로 보지 않습니다.
    url_ok = print_env_status("SUPABASE_URL", supabase_url, secret=False)
    anon_ok = print_env_status("SUPABASE_ANON_KEY", anon_key, secret=True)
    service_role_ok = print_env_status("SUPABASE_SERVICE_ROLE_KEY", service_role_key, secret=True)

    print("\n[Key usage guide]")
    print("- SUPABASE_ANON_KEY: RLS 정책과 함께 사용하는 공개용 key입니다.")
    print("- SUPABASE_SERVICE_ROLE_KEY: FastAPI 서버 코드에서만 사용하는 강한 권한의 key입니다.")
    print("- service role key는 Streamlit 화면, 브라우저 코드, GitHub에 노출하면 안 됩니다.")

    if not (url_ok and anon_ok and service_role_ok):
        print("\n[Next step]")
        print("1. Supabase Dashboard -> Project Settings -> API로 이동합니다.")
        print("2. Project URL, anon public key, service_role key를 복사합니다.")
        print("3. C:\\aidev\\02_supabase-ai-backend\\.env 파일에 값을 입력합니다.")
        return

    print("\nResult: Supabase 환경 변수가 준비되었습니다.")
    print("다음 챕터에서 Supabase 테이블을 만들고 CRUD 실습을 진행할 수 있습니다.")


if __name__ == "__main__":
    main()

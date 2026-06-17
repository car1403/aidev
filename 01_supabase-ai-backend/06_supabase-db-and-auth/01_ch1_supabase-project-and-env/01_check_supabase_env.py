from __future__ import annotations

import os

from dotenv import load_dotenv


def mask(value: str | None) -> str:
    """환경변수 값을 안전하게 확인하기 위해 앞뒤 일부만 보여줍니다.

    API key, service role key, Redis token은 비밀번호처럼 다루어야 합니다.
    수업 중 화면 공유를 할 수 있으므로 전체 값을 print하지 않습니다.
    """

    if not value:
        return "없음"
    if len(value) <= 12:
        return "설정됨, 하지만 길이가 짧아 실제 key인지 확인 필요"
    return f"{value[:6]}...{value[-4:]}"


def main() -> None:
    # load_dotenv는 현재 작업 폴더 또는 상위 폴더의 .env 값을 읽어 옵니다.
    # 이 스크립트는 C:\aidev\01_supabase-ai-backend에서 실행하는 것을 기준으로 합니다.
    load_dotenv()

    # os.getenv는 환경변수 값을 읽습니다.
    # 이름이 한 글자라도 다르면 None이 나오므로 변수명을 정확히 맞추어야 합니다.
    supabase_url = os.getenv("SUPABASE_URL")
    anon_key = os.getenv("SUPABASE_ANON_KEY")
    service_role_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    print("Supabase 환경변수 확인")
    print(f"SUPABASE_URL: {supabase_url or 'not set'}")
    print(f"SUPABASE_ANON_KEY: {mask(anon_key)}")
    print(f"SUPABASE_SERVICE_ROLE_KEY: {mask(service_role_key)}")

    # 필수 값 중 비어 있는 항목만 모읍니다.
    # 이렇게 하면 학생이 어떤 값을 빠뜨렸는지 바로 확인할 수 있습니다.
    missing = [
        name
        for name, value in {
            "SUPABASE_URL": supabase_url,
            "SUPABASE_ANON_KEY": anon_key,
            "SUPABASE_SERVICE_ROLE_KEY": service_role_key,
        }.items()
        if not value
    ]

    if missing:
        print("\n누락된 값:")
        for name in missing:
            print(f"- {name}")
        print("\n.env.example을 .env로 복사한 뒤 Supabase 값을 입력해 주세요.")
        return

    print("\nSupabase 실습에 필요한 환경변수가 설정되어 있습니다.")


if __name__ == "__main__":
    main()

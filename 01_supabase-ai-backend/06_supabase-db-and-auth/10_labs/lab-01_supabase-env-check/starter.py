"""Lab 01 starter - Supabase 환경변수 확인.

이 파일은 직접 빈칸을 채워 보며 환경변수 확인 흐름을 연습하는 starter입니다.
실제 정답 예시는 같은 폴더의 solution.py를 참고합니다.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv


def mask_secret(value: str) -> str:
    """키 전체가 노출되지 않도록 일부만 보여 주는 함수를 완성합니다."""

    # TODO: value 길이가 짧으면 "설정됨"만 반환합니다.
    # TODO: value 길이가 충분하면 앞 6글자와 뒤 4글자만 보여 줍니다.
    return value


def main() -> None:
    """환경변수 이름을 하나씩 확인합니다."""

    load_dotenv()

    required_names = [
        "SUPABASE_URL",
        "SUPABASE_ANON_KEY",
        "SUPABASE_SERVICE_ROLE_KEY",
    ]

    for name in required_names:
        value = os.getenv(name)

        # TODO: 값이 없으면 "없음"을 출력합니다.
        # TODO: 값이 있으면 mask_secret 함수를 사용해 안전하게 출력합니다.
        print(name, value)


if __name__ == "__main__":
    main()

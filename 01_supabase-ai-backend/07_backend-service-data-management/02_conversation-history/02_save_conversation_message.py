"""Supabase에 대화 묶음과 메시지를 저장하는 예제.

실행하면 conversations 테이블에 대화 묶음을 만들고,
messages 테이블에 user/assistant 메시지를 저장합니다.

실행 전 확인할 것:
1. C:\\aidev\\01_supabase-ai-backend\\.env 파일에 Supabase 값이 들어 있어야 합니다.
2. Supabase SQL Editor에서 06_supabase-db-and-auth/00_references/supabase-schema.sql을 실행해야 합니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from postgrest.exceptions import APIError
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_supabase() -> Client:
    """환경변수에서 Supabase 접속 정보를 읽어 client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError(
            "SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요."
        )

    return create_client(url, key)


def create_conversation(supabase: Client, title: str, user_id: str | None = None) -> dict:
    """새 대화 묶음을 생성합니다."""

    payload = {
        "title": title,
        "user_id": user_id,
    }

    result = supabase.table("conversations").insert(payload).execute()

    if not result.data:
        raise RuntimeError("대화 묶음 생성 결과가 비어 있습니다.")

    return result.data[0]


def add_message(supabase: Client, conversation_id: str, role: str, content: str) -> dict:
    """대화 묶음에 메시지 1개를 추가합니다."""

    # role은 user, assistant, system 중 하나여야 합니다.
    # 이 값은 화면에서 말풍선 방향을 나누는 기준으로도 사용할 수 있습니다.
    payload = {
        "conversation_id": conversation_id,
        "role": role,
        "content": content,
    }

    result = supabase.table("messages").insert(payload).execute()

    if not result.data:
        raise RuntimeError("메시지 저장 결과가 비어 있습니다.")

    return result.data[0]


def print_schema_help() -> None:
    """테이블이 없을 때 실행해야 할 SQL 파일 위치를 안내합니다."""

    print("\nSupabase 테이블이 없다면 SQL Editor에서 아래 파일을 먼저 실행하세요.")
    print(
        r"C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql"
    )


def main() -> None:
    """대화 묶음 생성 후 user/assistant 메시지를 저장합니다."""

    supabase = get_supabase()

    try:
        conversation = create_conversation(
            supabase=supabase,
            title="대화 이력 저장 실습",
        )
        conversation_id = conversation["id"]
        print("conversation_id:", conversation_id)

        user_message = add_message(
            supabase=supabase,
            conversation_id=conversation_id,
            role="user",
            content="대화 이력은 왜 Supabase에 저장하나요?",
        )
        print("user message id:", user_message["id"])

        assistant_message = add_message(
            supabase=supabase,
            conversation_id=conversation_id,
            role="assistant",
            content=(
                "사용자가 과거 대화를 다시 볼 수 있고, "
                "서비스 품질 분석에도 사용할 수 있기 때문입니다."
            ),
        )
        print("assistant message id:", assistant_message["id"])

    except APIError as error:
        print("Supabase 대화 이력 저장 중 오류가 발생했습니다.")
        print(f"오류 내용: {error}")
        print_schema_help()


if __name__ == "__main__":
    main()

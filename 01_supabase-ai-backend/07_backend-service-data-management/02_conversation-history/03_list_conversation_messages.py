"""Supabase에서 특정 대화방의 메시지를 조회하는 예제.

실행 전 `02_save_conversation_message.py`로 만든 conversation_id를
아래 변수에 넣어 조회할 수 있습니다.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_supabase() -> Client:
    """Supabase client를 생성합니다."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요.")

    return create_client(url, key)


def list_messages(supabase: Client, conversation_id: str) -> list[dict]:
    """conversation_id에 속한 메시지를 생성 시간 순서로 조회합니다."""

    result = (
        supabase.table("messages")
        .select("*")
        .eq("conversation_id", conversation_id)
        .order("created_at")
        .execute()
    )
    return result.data


def main() -> None:
    supabase = get_supabase()

    conversation_id = input("조회할 conversation_id를 입력하세요: ").strip()
    messages = list_messages(supabase, conversation_id)

    print("\n메시지 목록:")
    for message in messages:
        print(f"[{message['role']}] {message['content']}")


if __name__ == "__main__":
    main()

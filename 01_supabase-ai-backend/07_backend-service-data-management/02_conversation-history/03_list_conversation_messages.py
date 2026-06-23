"""Supabase에서 특정 대화의 메시지를 조회하는 예제.

먼저 02_save_conversation_message.py를 실행합니다.
그때 출력된 conversation_id를 이 파일에서 입력하면 해당 대화의 메시지를 조회할 수 있습니다.
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
    """conversation_id를 입력받아 메시지 목록을 출력합니다."""

    supabase = get_supabase()

    conversation_id = input("조회할 conversation_id를 입력하세요: ").strip()

    if not conversation_id:
        print("conversation_id가 비어 있습니다.")
        return

    try:
        messages = list_messages(supabase, conversation_id)
    except APIError as error:
        print("Supabase 메시지 조회 중 오류가 발생했습니다.")
        print(f"오류 내용: {error}")
        return

    if not messages:
        print("조회된 메시지가 없습니다.")
        return

    print("\n메시지 목록:")
    for index, message in enumerate(messages, start=1):
        print(f"{index}. [{message['role']}] {message['content']}")


if __name__ == "__main__":
    main()

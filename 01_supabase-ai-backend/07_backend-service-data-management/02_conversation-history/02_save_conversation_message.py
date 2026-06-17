"""Supabase에 대화방과 메시지를 저장하는 예제.

실행하면 conversations 테이블에 대화방을 만들고,
messages 테이블에 user/assistant 메시지를 저장합니다.
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


def create_conversation(supabase: Client, title: str) -> dict:
    """새 대화방을 생성합니다."""

    result = supabase.table("conversations").insert({"title": title}).execute()
    if not result.data:
        raise RuntimeError("대화방 생성 결과가 비어 있습니다.")
    return result.data[0]


def add_message(supabase: Client, conversation_id: str, role: str, content: str) -> dict:
    """대화방에 메시지를 1개 추가합니다."""

    # role은 user, assistant, system 중 하나여야 합니다.
    # 이 값은 나중에 화면에서 말풍선 방향을 나누는 기준으로도 사용할 수 있습니다.
    result = (
        supabase.table("messages")
        .insert(
            {
                "conversation_id": conversation_id,
                "role": role,
                "content": content,
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("메시지 저장 결과가 비어 있습니다.")

    return result.data[0]


def main() -> None:
    supabase = get_supabase()

    conversation = create_conversation(supabase, "대화 이력 저장 실습")
    conversation_id = conversation["id"]
    print("conversation_id:", conversation_id)

    user_message = add_message(
        supabase,
        conversation_id,
        "user",
        "대화 이력은 왜 Supabase에 저장하나요?",
    )
    print("user message:", user_message["id"])

    assistant_message = add_message(
        supabase,
        conversation_id,
        "assistant",
        "사용자가 과거 대화를 다시 볼 수 있고, 서비스 품질 분석에도 사용할 수 있기 때문입니다.",
    )
    print("assistant message:", assistant_message["id"])


if __name__ == "__main__":
    main()

"""Supabase에 대화 이력과 서비스 로그를 저장하는 예제.

AI 백엔드 서비스에서는 답변을 생성하는 것만큼 기록을 남기는 것도 중요합니다.
사용자가 어떤 대화를 했는지, 서버가 어떤 이벤트를 처리했는지 Supabase에
저장하면 나중에 화면 조회, 오류 분석, 품질 개선에 사용할 수 있습니다.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from supabase import Client, create_client


def get_supabase() -> Client:
    """Supabase client를 생성합니다."""

    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY를 .env에 설정해 주세요.")

    return create_client(url, key)


def create_conversation(supabase: Client) -> dict:
    """새 대화 세션을 만듭니다."""

    # user_id는 Auth를 본격 적용하기 전에는 비워 둘 수 있습니다.
    # 실제 서비스에서는 로그인한 사용자의 id를 넣습니다.
    result = (
        supabase.table("conversations")
        .insert({"title": "Supabase 대화 이력 저장 실습"})
        .execute()
    )

    if not result.data:
        raise RuntimeError("conversation 생성 결과가 비어 있습니다.")

    return result.data[0]


def add_message(supabase: Client, conversation_id: str, role: str, content: str) -> dict:
    """대화방에 user 또는 assistant 메시지를 추가합니다."""

    # role은 user, assistant, system 중 하나여야 합니다.
    # 이 제약은 supabase-schema.sql의 check 조건과 연결됩니다.
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
        raise RuntimeError("message 생성 결과가 비어 있습니다.")

    return result.data[0]


def add_service_log(supabase: Client, event_type: str, message: str, metadata: dict) -> dict:
    """서비스 실행 로그를 저장합니다."""

    # metadata는 jsonb 컬럼에 저장됩니다.
    # 처리 시간, 모델 이름, 요청 id처럼 구조가 자주 바뀌는 값을 담기 좋습니다.
    result = (
        supabase.table("service_logs")
        .insert(
            {
                "event_type": event_type,
                "message": message,
                "metadata": metadata,
            }
        )
        .execute()
    )

    if not result.data:
        raise RuntimeError("service log 생성 결과가 비어 있습니다.")

    return result.data[0]


def main() -> None:
    supabase = get_supabase()

    conversation = create_conversation(supabase)
    conversation_id = conversation["id"]
    print("Conversation created:", conversation_id)

    user_message = add_message(
        supabase,
        conversation_id=conversation_id,
        role="user",
        content="Supabase에는 어떤 데이터를 저장하면 좋나요?",
    )
    print("User message:", user_message["id"])

    assistant_message = add_message(
        supabase,
        conversation_id=conversation_id,
        role="assistant",
        content="대화 이력, 서비스 로그, 사용자 피드백처럼 나중에 다시 볼 데이터가 좋습니다.",
    )
    print("Assistant message:", assistant_message["id"])

    log = add_service_log(
        supabase,
        event_type="conversation.created",
        message="대화 이력 저장 실습이 완료되었습니다.",
        metadata={
            "conversation_id": conversation_id,
            "message_count": 2,
            "storage": "supabase",
        },
    )
    print("Service log:", log["id"])


if __name__ == "__main__":
    main()

"""Supabase에 대화 이력과 서비스 로그를 저장하는 예제입니다.

AI 백엔드 서비스에서는 답변을 생성하는 것만큼 기록을 남기는 것도 중요합니다.
사용자가 어떤 대화를 했는지, 서버가 어떤 이벤트를 처리했는지 Supabase에 저장하면
나중에 화면 조회, 오류 분석, 품질 개선에 활용할 수 있습니다.
"""

from __future__ import annotations

import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from postgrest.exceptions import APIError
from supabase import Client, create_client


# 이 파일은 다음 위치에 있습니다.
# 02_supabase-ai-backend/03_supabase-db-and-auth/05_conversation-history-and-service-logs/01_insert_conversation_and_log.py
# parents[2]는 02_supabase-ai-backend 폴더입니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다."""

    if value is None:
        return False

    return value.strip().startswith(("your-", "https://your-"))


def get_required_env(name: str) -> str:
    """필수 환경 변수를 읽고, 없으면 이해하기 쉬운 오류를 발생시킵니다."""

    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"{name} 값이 없습니다. C:\\aidev\\02_supabase-ai-backend\\.env 파일을 확인하세요.")

    cleaned = value.strip()
    if is_placeholder(cleaned):
        raise RuntimeError(f"{name} 값이 예시 값입니다. Supabase Dashboard에서 실제 값을 복사해 넣어 주세요.")

    return cleaned


def get_supabase() -> Client:
    """Supabase client를 생성합니다.

    이 예제는 백엔드 서버 코드 관점의 실습이므로 service role key를 사용합니다.
    service role key는 강한 권한을 가진 key이므로 화면 코드나 GitHub에 노출하면 안 됩니다.
    """

    load_dotenv(ENV_PATH)

    url = get_required_env("SUPABASE_URL")
    service_role_key = get_required_env("SUPABASE_SERVICE_ROLE_KEY")

    return create_client(url, service_role_key)


def create_conversation(supabase: Client, title: str) -> dict:
    """conversations 테이블에 새 대화방을 만듭니다."""

    # user_id는 Auth를 본격 적용하기 전에는 비워 둘 수 있습니다.
    # 실제 서비스에서는 로그인한 사용자의 id를 넣습니다.
    result = supabase.table("conversations").insert({"title": title}).execute()

    if not result.data:
        raise RuntimeError("conversation 생성 결과가 비어 있습니다. 테이블과 권한을 확인하세요.")

    return result.data[0]


def add_message(supabase: Client, conversation_id: str, role: str, content: str) -> dict:
    """messages 테이블에 user 또는 assistant 메시지를 추가합니다."""

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
        raise RuntimeError("message 생성 결과가 비어 있습니다. conversation_id와 테이블 권한을 확인하세요.")

    return result.data[0]


def add_service_log(supabase: Client, event_type: str, message: str, metadata: dict) -> dict:
    """service_logs 테이블에 서비스 실행 로그를 저장합니다."""

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
        raise RuntimeError("service log 생성 결과가 비어 있습니다. service_logs 테이블을 확인하세요.")

    return result.data[0]


def list_messages(supabase: Client, conversation_id: str) -> list[dict]:
    """특정 대화방에 저장된 메시지 목록을 조회합니다."""

    result = (
        supabase.table("messages")
        .select("*")
        .eq("conversation_id", conversation_id)
        .order("created_at")
        .execute()
    )

    return result.data


def list_recent_service_logs(supabase: Client, limit: int = 5) -> list[dict]:
    """최근 서비스 로그를 조회합니다."""

    result = (
        supabase.table("service_logs")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return result.data


def print_supabase_setup_help(error: APIError) -> None:
    """Supabase 테이블이 없을 때 확인할 내용을 안내합니다."""

    print("[Supabase 실행 오류]")
    print(error)
    print("\n확인할 내용:")
    print("1. Supabase Dashboard -> SQL Editor를 엽니다.")
    print("2. 03_supabase-db-and-auth/00_references/supabase-schema.sql 내용을 실행합니다.")
    print("3. Table Editor에서 conversations, messages, service_logs 테이블이 보이는지 확인합니다.")
    print("4. 테이블을 만든 뒤 이 예제를 다시 실행합니다.")


def main() -> None:
    """대화방, 메시지, 서비스 로그 저장 흐름을 차례대로 실행합니다."""

    supabase = get_supabase()

    try:
        conversation = create_conversation(supabase, title="Supabase 대화 이력 저장 실습")
        conversation_id = conversation["id"]
        print("[conversation created]")
        pprint(conversation, width=100)

        user_message = add_message(
            supabase,
            conversation_id=conversation_id,
            role="user",
            content="Supabase에는 어떤 데이터를 저장하면 좋나요?",
        )
        print("\n[user message saved]")
        pprint(user_message, width=100)

        assistant_message = add_message(
            supabase,
            conversation_id=conversation_id,
            role="assistant",
            content="대화 이력, 서비스 로그, 사용자 피드백처럼 나중에 다시 볼 데이터는 Supabase에 저장하는 것이 좋습니다.",
        )
        print("\n[assistant message saved]")
        pprint(assistant_message, width=100)

        log = add_service_log(
            supabase,
            event_type="conversation.created",
            message="대화 이력 저장 실습이 완료되었습니다.",
            metadata={
                "conversation_id": conversation_id,
                "message_count": 2,
                "storage": "supabase",
                "provider": "gemini",
                "actual_api_called": False,
                "model": "gemini-2.5-flash-lite",
                "llm_call_mode": "mock-first",
                "project_default_call": "Gemini SDK",
                "reference_endpoint": "02_llm-api-integration/05_fastapi-llm-endpoint/02_gemini_sdk_endpoint.py",
            },
        )
        print("\n[service log saved]")
        pprint(log, width=100)

        print("\n[messages in this conversation]")
        pprint(list_messages(supabase, conversation_id), width=100)

        print("\n[recent service logs]")
        pprint(list_recent_service_logs(supabase), width=100)

        print("\nResult: 대화방, 메시지, 서비스 로그 저장 흐름을 확인했습니다.")
    except APIError as error:
        print_supabase_setup_help(error)


if __name__ == "__main__":
    main()

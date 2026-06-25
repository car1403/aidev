from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client


# 이 파일은 다음 위치에 있습니다.
# 02_supabase-ai-backend/06_supabase-db-and-auth/02_supabase-table-and-crud/01_learning_notes_crud.py
# parents[2]는 02_supabase-ai-backend 폴더입니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def is_placeholder(value: str | None) -> bool:
    """예시 값인지 확인합니다.

    .env.example에 들어 있는 your-supabase-service-role-key 같은 값은
    실제 Supabase key가 아니므로 API 호출에 사용하면 안 됩니다.
    """

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

    Supabase client는 Python 코드에서 Supabase REST API를 쉽게 호출하도록 도와주는 객체입니다.

    이 예제는 백엔드 서버 코드 관점의 실습이므로 service role key를 사용합니다.
    service role key는 강한 권한을 가진 key이므로 화면 코드나 GitHub에 노출하면 안 됩니다.
    """

    load_dotenv(ENV_PATH)

    url = get_required_env("SUPABASE_URL")
    service_role_key = get_required_env("SUPABASE_SERVICE_ROLE_KEY")

    return create_client(url, service_role_key)


def create_note(supabase: Client) -> dict:
    """learning_notes 테이블에 실습용 메모를 1개 저장합니다."""

    # insert는 SQL의 INSERT INTO와 비슷합니다.
    # 딕셔너리의 key는 테이블 컬럼명과 같아야 합니다.
    result = (
        supabase.table("learning_notes")
        .insert(
            {
                "title": "Supabase CRUD practice",
                "content": "Python에서 insert, select, update, delete를 차례대로 실행합니다.",
            }
        )
        .execute()
    )

    # Supabase 응답의 data에는 생성된 행 정보가 들어 있습니다.
    if not result.data:
        raise RuntimeError("insert 결과가 비어 있습니다. learning_notes 테이블과 권한을 확인하세요.")

    return result.data[0]


def list_recent_notes(supabase: Client) -> list[dict]:
    """최근 학습 메모 5개를 조회합니다."""

    # select("*")는 모든 컬럼을 조회한다는 뜻입니다.
    # order("created_at", desc=True)는 최신 데이터가 먼저 보이도록 정렬합니다.
    # limit(5)는 너무 많은 데이터를 가져오지 않도록 최대 5개만 조회합니다.
    result = (
        supabase.table("learning_notes")
        .select("*")
        .order("created_at", desc=True)
        .limit(5)
        .execute()
    )

    return result.data


def update_note_title(supabase: Client, note_id: str) -> dict:
    """방금 만든 실습 메모의 제목을 수정합니다."""

    # update와 delete에는 조건이 중요합니다.
    # eq("id", note_id)는 id 컬럼 값이 note_id와 같은 행만 대상으로 삼겠다는 뜻입니다.
    result = (
        supabase.table("learning_notes")
        .update({"title": "Supabase CRUD practice - updated"})
        .eq("id", note_id)
        .execute()
    )

    if not result.data:
        raise RuntimeError("update 결과가 비어 있습니다. note_id와 테이블 권한을 확인하세요.")

    return result.data[0]


def delete_note(supabase: Client, note_id: str) -> None:
    """실습으로 만든 메모를 삭제합니다."""

    # delete도 update와 마찬가지로 조건을 붙여야 안전합니다.
    # 조건이 없으면 의도하지 않은 데이터가 삭제될 수 있습니다.
    supabase.table("learning_notes").delete().eq("id", note_id).execute()


def print_note(label: str, note: dict) -> None:
    """메모 한 개를 보기 좋게 출력합니다."""

    print(f"\n[{label}]")
    print(f"id: {note.get('id')}")
    print(f"title: {note.get('title')}")
    print(f"content: {note.get('content')}")
    print(f"created_at: {note.get('created_at')}")


def main() -> None:
    """CRUD 흐름을 create -> read -> update -> delete 순서로 실행합니다."""

    supabase = get_supabase()

    created = create_note(supabase)
    print_note("created note", created)

    notes = list_recent_notes(supabase)
    print("\n[recent notes]")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note.get('title')} - {note.get('content')}")

    updated = update_note_title(supabase, created["id"])
    print_note("updated note", updated)

    delete_note(supabase, created["id"])
    print(f"\n[deleted practice note]\n{created['id']}")

    print("\nResult: insert/select/update/delete 흐름을 모두 실행했습니다.")


if __name__ == "__main__":
    main()

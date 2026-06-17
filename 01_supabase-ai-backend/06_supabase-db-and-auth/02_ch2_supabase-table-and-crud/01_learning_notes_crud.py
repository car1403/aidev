from __future__ import annotations

import os

from dotenv import load_dotenv
from supabase import Client, create_client


def get_supabase() -> Client:
    """Supabase client를 생성합니다.

    Supabase client는 Python 코드에서 Supabase REST API를 쉽게 호출하도록 도와줍니다.
    이 과정에서는 서버 코드 기준으로 service role key를 우선 사용합니다.
    단, service role key는 강한 권한을 가지므로 프론트엔드에 노출하면 안 됩니다.
    """

    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY or SUPABASE_ANON_KEY are required.")

    return create_client(url, key)


def create_note(supabase: Client) -> dict:
    """learning_notes 테이블에 새 학습 메모를 저장합니다."""

    # insert는 SQL의 INSERT INTO와 비슷합니다.
    # 딕셔너리 key는 테이블 컬럼명과 같아야 합니다.
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

    if not result.data:
        raise RuntimeError("learning_notes insert 결과가 비어 있습니다.")

    return result.data[0]


def list_recent_notes(supabase: Client) -> list[dict]:
    """최근 학습 메모 5개를 조회합니다."""

    # select("*")는 모든 컬럼을 조회한다는 뜻입니다.
    # order(..., desc=True)는 최신 데이터가 먼저 보이도록 정렬합니다.
    result = (
        supabase.table("learning_notes")
        .select("*")
        .order("created_at", desc=True)
        .limit(5)
        .execute()
    )
    return result.data


def update_note_title(supabase: Client, note_id: str) -> dict:
    """방금 만든 학습 메모의 제목을 수정합니다."""

    # update를 할 때는 eq("id", note_id)처럼 조건을 반드시 붙입니다.
    # 조건이 없으면 여러 행이 바뀔 수 있으므로 매우 위험합니다.
    result = (
        supabase.table("learning_notes")
        .update({"title": "Supabase CRUD practice - updated"})
        .eq("id", note_id)
        .execute()
    )

    if not result.data:
        raise RuntimeError("learning_notes update 결과가 비어 있습니다.")

    return result.data[0]


def delete_note(supabase: Client, note_id: str) -> None:
    """실습으로 만든 학습 메모를 삭제합니다."""

    # delete도 update와 마찬가지로 조건을 반드시 붙입니다.
    supabase.table("learning_notes").delete().eq("id", note_id).execute()


def main() -> None:
    supabase = get_supabase()

    created = create_note(supabase)
    print("Created:")
    print(created)

    notes = list_recent_notes(supabase)
    print("\nLatest notes:")
    for note in notes:
        print(f"- {note['title']}: {note['content']}")

    updated = update_note_title(supabase, created["id"])
    print("\nUpdated:")
    print(updated)

    delete_note(supabase, created["id"])
    print("\nDeleted practice note:")
    print(created["id"])


if __name__ == "__main__":
    main()

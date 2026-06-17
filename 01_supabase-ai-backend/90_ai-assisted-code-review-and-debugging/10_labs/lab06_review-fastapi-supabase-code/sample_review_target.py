"""코드 리뷰 실습용 FastAPI + Supabase 예제.

이 파일은 일부러 개선할 부분을 남겨 둔 리뷰 대상 코드입니다.
실제 서비스 코드로 사용하지 않습니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Review Target")


class NoteRequest(BaseModel):
    # 질문: title/content에 길이 제한이나 빈 문자열 검증이 있나요?
    title: str
    content: str


def get_fake_supabase_client():
    """리뷰 실습을 위해 Supabase client를 흉내 냅니다."""

    return None


@app.post("/notes")
def create_note(request: NoteRequest):
    """학습 메모를 생성하는 endpoint입니다."""

    supabase = get_fake_supabase_client()

    # 리뷰 포인트:
    # 1. supabase가 None일 때 어떤 오류가 날까요?
    # 2. insert 결과가 비어 있으면 어떻게 처리해야 할까요?
    # 3. 실제 코드라면 환경변수와 key를 어떻게 관리해야 할까요?
    result = {
        "title": request.title,
        "content": request.content,
    }

    return {"item": result, "supabase": str(supabase)}


@app.delete("/notes")
def delete_all_notes():
    """리뷰 실습용 위험한 endpoint입니다."""

    # 리뷰 포인트:
    # 실제 Supabase delete 코드에서 조건 없이 삭제하면 매우 위험합니다.
    # delete().eq("id", note_id)처럼 삭제 대상을 제한해야 합니다.
    return {"message": "조건 없는 삭제는 위험합니다."}

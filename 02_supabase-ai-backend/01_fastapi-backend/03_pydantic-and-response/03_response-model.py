"""Response Model 예제입니다.

이 파일은 Response Model 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

response_model은 API 응답으로 내보낼 데이터의 모양을 제한합니다.
내부 데이터에 internal_note 같은 값이 있어도 응답 모델에 없으면 밖으로 나가지 않습니다.
"""

from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Response Model Practice")


class MemoPublic(BaseModel):
    """외부에 공개해도 되는 메모 응답 모델입니다."""

    id: int
    title: str
    content: str
    tags: list[str]


memos: dict[int, dict[str, Any]] = {
    1: {
        "id": 1,
        "title": "응답 모델 연습",
        "content": "response_model이 어떤 필드를 내보내는지 확인합니다.",
        "tags": ["response"],
        # 이 값은 서버 내부에서만 쓰는 값입니다.
        # MemoPublic에 없기 때문에 응답에는 포함되지 않습니다.
        "internal_note": "응답으로 내보내면 안 되는 내부 메모입니다.",
    }
}


@app.get("/memos/{memo_id}", response_model=MemoPublic)
def get_memo(memo_id: int):
    """메모 정보를 반환하지만 internal_note는 응답에서 제외됩니다."""

    if memo_id not in memos:
        raise HTTPException(status_code=404, detail="Memo not found")

    return memos[memo_id]

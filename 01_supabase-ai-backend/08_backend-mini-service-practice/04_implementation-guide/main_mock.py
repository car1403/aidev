"""AI 질문 응답 백엔드 미니 서비스 mock 구현.

이 파일은 Supabase나 실제 LLM API를 호출하지 않습니다.
메모리 리스트에 데이터를 저장하므로 수업에서 가장 먼저 실행하기 좋습니다.
"""

from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI, HTTPException

from llm_mock import generate_mock_answer
from schemas import QaCreate
from service_logger import build_service_log, now_iso


app = FastAPI(title="AI QA Mini Service Mock")


# 서버가 실행되는 동안만 유지되는 메모리 저장소입니다.
# 실제 서비스에서는 이 데이터가 Supabase 테이블에 저장됩니다.
qa_items: list[dict] = []
service_logs: list[dict] = []


@app.get("/health")
def health() -> dict[str, str]:
    """서버 상태를 확인합니다."""

    return {"status": "ok", "storage": "memory", "llm": "mock"}


@app.post("/qa", status_code=201)
def create_qa(request: QaCreate) -> dict[str, dict]:
    """사용자 질문을 받고 mock AI 답변을 생성합니다."""

    answer = generate_mock_answer(request.question, request.model)

    item = {
        "id": str(uuid4()),
        "user_id": request.user_id,
        "question": request.question,
        "answer": answer,
        "model": request.model,
        "created_at": now_iso(),
    }
    qa_items.append(item)

    # 서비스 로그는 "어떤 일이 일어났는지"를 기록합니다.
    service_logs.append(
        build_service_log(
            event_type="qa.created",
            message="질문/답변이 생성되었습니다.",
            metadata={
                "qa_item_id": item["id"],
                "model": request.model,
                "storage": "memory",
            },
        )
    )

    return {"item": item}


@app.get("/qa")
def list_qa() -> dict[str, list[dict]]:
    """저장된 질문/답변 목록을 조회합니다."""

    return {"items": qa_items}


@app.get("/qa/{item_id}")
def get_qa(item_id: str) -> dict[str, dict]:
    """id로 질문/답변 1개를 조회합니다."""

    for item in qa_items:
        if item["id"] == item_id:
            return {"item": item}

    raise HTTPException(status_code=404, detail="QA item not found.")


@app.get("/service-logs")
def list_service_logs() -> dict[str, list[dict]]:
    """서비스 로그 목록을 조회합니다."""

    return {"items": service_logs}

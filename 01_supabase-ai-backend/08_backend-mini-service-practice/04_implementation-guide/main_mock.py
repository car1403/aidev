"""AI 질문 응답 백엔드 미니 서비스 mock 구현.

이 파일은 Supabase나 실제 LLM API를 호출하지 않습니다.
데이터를 메모리 리스트에 저장하므로 API 구조를 가장 먼저 확인하기 좋습니다.
"""

from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query

from llm_mock import generate_mock_answer
from schemas import QuestionCreateRequest, ServiceLogCreateRequest
from service_logger import build_service_log, now_iso


app = FastAPI(title="AI Question Mini Service Mock")


# 서버가 실행되는 동안만 유지되는 메모리 저장소입니다.
# 서버를 재시작하면 아래 리스트에 들어 있던 데이터는 모두 사라집니다.
question_items: list[dict] = []
service_logs: list[dict] = []


@app.get("/health")
def health() -> dict[str, str | bool]:
    """서버 상태를 확인합니다."""

    return {
        "ok": True,
        "status": "healthy",
        "service": "backend-mini-service",
        "storage": "memory",
        "llm": "mock",
    }


@app.post("/questions", status_code=201)
def create_question(request: QuestionCreateRequest) -> dict[str, bool | dict]:
    """사용자 질문을 받고 mock AI 답변을 생성합니다."""

    # 1. mock LLM 함수로 답변을 만듭니다.
    answer = generate_mock_answer(request.question, request.model)

    # 2. 질문과 답변을 하나의 dict로 묶습니다.
    item = {
        "id": str(uuid4()),
        "user_id": request.user_id,
        "question": request.question,
        "answer": answer,
        "model": request.model,
        "created_at": now_iso(),
    }

    # 3. 실제 서비스라면 이 위치에서 Supabase에 insert합니다.
    question_items.append(item)

    # 4. 처리 결과를 로그로 남깁니다.
    service_logs.append(
        build_service_log(
            event_type="question_created",
            message="질문 답변 생성 성공",
            metadata={
                "question_id": item["id"],
                "user_id": request.user_id,
                "model": request.model,
                "storage": "memory",
            },
        )
    )

    return {"ok": True, "item": item}


@app.get("/questions")
def list_questions(
    user_id: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
) -> dict[str, bool | list[dict]]:
    """저장된 질문/답변 목록을 조회합니다."""

    # user_id가 들어오면 해당 사용자 데이터만 남깁니다.
    items = question_items
    if user_id:
        items = [item for item in question_items if item["user_id"] == user_id]

    # 최신 데이터가 앞에 오도록 뒤집은 뒤 limit 개수만 반환합니다.
    return {"ok": True, "items": list(reversed(items))[:limit]}


@app.get("/questions/{question_id}")
def get_question(question_id: str) -> dict[str, bool | dict]:
    """id로 질문/답변 1개를 조회합니다."""

    for item in question_items:
        if item["id"] == question_id:
            return {"ok": True, "item": item}

    raise HTTPException(
        status_code=404,
        detail={
            "code": "question_not_found",
            "message": "질문 기록을 찾을 수 없습니다.",
        },
    )


@app.post("/service-logs", status_code=201)
def create_service_log(request: ServiceLogCreateRequest) -> dict[str, bool | dict]:
    """서비스 로그를 직접 저장합니다."""

    log_item = build_service_log(
        event_type=request.event_type,
        message=request.message,
        metadata=request.metadata,
    )
    service_logs.append(log_item)

    return {"ok": True, "item": log_item}


@app.get("/service-logs")
def list_service_logs(
    event_type: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
) -> dict[str, bool | list[dict]]:
    """서비스 로그 목록을 조회합니다."""

    logs = service_logs
    if event_type:
        logs = [log for log in service_logs if log["event_type"] == event_type]

    return {"ok": True, "items": list(reversed(logs))[:limit]}

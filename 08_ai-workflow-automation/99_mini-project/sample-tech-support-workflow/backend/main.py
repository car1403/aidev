"""FastAPI backend for the sample tech support workflow."""

from fastapi import FastAPI

from backend.schemas import TicketAnalysis, TicketRequest
from backend.workflow import WorkflowStore, run_workflow

app = FastAPI(title="Tech Support Workflow API")
store = WorkflowStore()


@app.get("/health")
def health() -> dict[str, str]:
    """서비스 상태 확인용 API입니다."""

    return {"status": "ok", "service": "tech-support-workflow"}


@app.post("/analyze", response_model=TicketAnalysis)
def analyze(ticket: TicketRequest) -> TicketAnalysis:
    """기술 지원 문의를 분석하고 다음 Action을 결정합니다."""

    return run_workflow(ticket, store)


@app.get("/events")
def events() -> list[dict[str, str]]:
    """워크플로우 실행 이벤트를 최신순으로 반환합니다."""

    return list(reversed(store.events))


@app.get("/metrics")
def metrics() -> dict[str, float | int]:
    """운영 대시보드에서 사용할 간단한 지표입니다."""

    urgent_rate = store.urgent_runs / store.total_runs if store.total_runs else 0
    validation_failure_rate = store.validation_failures / store.total_runs if store.total_runs else 0
    return {
        "total_runs": store.total_runs,
        "urgent_runs": store.urgent_runs,
        "urgent_rate": round(urgent_rate, 3),
        "validation_failures": store.validation_failures,
        "validation_failure_rate": round(validation_failure_rate, 3),
    }

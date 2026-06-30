import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.log_schema import LogCreate, LogItem, LogSummary
from app.services.db_service import list_logs, save_log, summarize_logs
from app.services.event_service import event_stream, publish_log_event


router = APIRouter(tags=["logs"])


@router.post("/logs", response_model=LogItem)
async def create_log(payload: LogCreate) -> dict:
    item = save_log(payload.model_dump())
    await publish_log_event(item)
    return item


@router.get("/logs", response_model=list[LogItem])
def get_logs(limit: int = 50) -> list[dict]:
    return list_logs(limit)


@router.get("/logs/summary", response_model=list[LogSummary])
def get_log_summary() -> list[dict]:
    return summarize_logs()


@router.get("/stream/logs")
async def stream_logs() -> StreamingResponse:
    async def generate():
        async for item in event_stream():
            data = json.dumps(item, ensure_ascii=False)
            yield f"event: log\ndata: {data}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")

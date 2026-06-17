"""서비스 로그 생성 보조 함수.

로그는 서비스가 어떤 일을 했는지 나중에 확인하기 위한 기록입니다.
성공/실패, endpoint, model, 저장된 item id 같은 정보를 metadata에 담습니다.
"""

from datetime import datetime, timezone
from uuid import uuid4


def now_iso() -> str:
    """UTC 현재 시간을 ISO 문자열로 반환합니다."""

    return datetime.now(timezone.utc).isoformat()


def build_service_log(event_type: str, message: str, metadata: dict | None = None) -> dict:
    """메모리 저장소나 Supabase에 저장할 서비스 로그 dict를 만듭니다."""

    return {
        "id": str(uuid4()),
        "event_type": event_type,
        "message": message,
        "metadata": metadata or {},
        "created_at": now_iso(),
    }

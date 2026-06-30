from fastapi import APIRouter, Depends

from app.core.security import parse_bearer_token
from app.schemas.log_schema import ServiceLogItem
from app.services.auth_service import get_user_by_token
from app.services.log_service import list_logs_for_user


router = APIRouter(tags=["logs"])


@router.get("/service-logs", response_model=list[ServiceLogItem])
def service_logs_endpoint(token: str = Depends(parse_bearer_token)) -> list[dict]:
    user = get_user_by_token(token)
    return list_logs_for_user(user["email"])

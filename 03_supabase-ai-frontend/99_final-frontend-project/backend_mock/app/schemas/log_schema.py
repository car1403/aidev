from pydantic import BaseModel


class ServiceLogItem(BaseModel):
    id: str
    user_email: str | None = None
    action: str
    status: str
    detail: str | None = None
    created_at: str

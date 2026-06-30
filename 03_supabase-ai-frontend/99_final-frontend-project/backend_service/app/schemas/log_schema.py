from pydantic import BaseModel


class ServiceLogResponse(BaseModel):
    id: str
    action: str
    status: str
    message: str | None = None
    created_at: str | None = None

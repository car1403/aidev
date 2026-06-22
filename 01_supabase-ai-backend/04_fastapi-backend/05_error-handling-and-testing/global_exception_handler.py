"""전역 예외 처리(Exception Handler) 예제.

서비스를 만들다 보면 오류가 여러 곳에서 발생합니다.
각 API마다 오류 응답 형식이 다르면 프론트엔드가 처리하기 어렵습니다.

전역 예외 처리는 특정 오류가 발생했을 때 응답 모양을 하나로 맞추는 방법입니다.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(title="Global Exception Handler Practice")


class ServiceError(Exception):
    """서비스 규칙 위반을 표현하기 위한 수업용 예외 클래스입니다.

    Python 기본 예외를 그대로 사용해도 되지만,
    이렇게 직접 예외 클래스를 만들면 "우리 서비스에서 의도한 오류"를
    더 명확하게 구분할 수 있습니다.
    """

    def __init__(self, error_code: str, message: str, status_code: int = 400):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code


@app.exception_handler(ServiceError)
def handle_service_error(request, exc: ServiceError):
    """ServiceError가 발생하면 항상 같은 JSON 형식으로 응답합니다."""

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.error_code,
                "message": exc.message,
            },
        },
    )


items = {
    1: {"id": 1, "name": "Python note"},
    2: {"id": 2, "name": "FastAPI note"},
}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """상품을 조회하고, 없으면 표준 오류 응답을 반환합니다."""

    if item_id not in items:
        raise ServiceError(
            error_code="ITEM_NOT_FOUND",
            message="요청한 상품을 찾을 수 없습니다.",
            status_code=404,
        )

    return {
        "success": True,
        "data": items[item_id],
    }

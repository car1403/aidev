"""외부 API 호출 구조 예제.

실제 외부 API를 호출할 때는 httpx.AsyncClient를 자주 사용합니다.
이 예제는 네트워크가 가능한 공개 테스트 API를 호출합니다.
"""

import httpx
from fastapi import FastAPI, HTTPException


app = FastAPI(title="External API Structure Practice")


@app.get("/external/posts/{post_id}")
async def get_external_post(post_id: int):
    """외부 API에서 게시글 하나를 가져와 우리 API 응답으로 반환합니다."""

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail="External API returned an error",
        ) from error
    except httpx.RequestError as error:
        raise HTTPException(
            status_code=503,
            detail="External API is not reachable",
        ) from error

    external_data = response.json()

    return {
        "source": "jsonplaceholder",
        "data": {
            "id": external_data["id"],
            "title": external_data["title"],
            "body_preview": external_data["body"][:60],
        },
    }

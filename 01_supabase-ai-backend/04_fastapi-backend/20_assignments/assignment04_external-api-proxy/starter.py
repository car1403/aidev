"""Assignment 04 starter: External API Proxy.

요구사항:
1. async endpoint 작성
2. httpx.AsyncClient 사용
3. 외부 API 실패 시 HTTPException 반환
"""

import httpx
from fastapi import FastAPI, HTTPException


app = FastAPI(title="External API Proxy Assignment")


@app.get("/proxy/posts/{post_id}")
async def proxy_post(post_id: int):
    """외부 테스트 API의 post 데이터를 우리 API 형식으로 반환합니다."""

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as error:
        raise HTTPException(status_code=error.response.status_code, detail="External API error") from error
    except httpx.RequestError as error:
        raise HTTPException(status_code=503, detail="External API unavailable") from error

    # TODO: 필요한 필드만 골라 반환하세요.
    return {"data": response.json()}

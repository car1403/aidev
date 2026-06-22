"""외부 API 호출 구조 예제입니다.

이 파일은 외부 API 호출 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

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
        # AsyncClient는 async 함수 안에서 외부 HTTP 요청을 보낼 때 사용합니다.
        # timeout=5는 외부 API가 너무 오래 응답하지 않을 때 5초 뒤 중단하기 위한 설정입니다.
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
        # raw 데이터 전체를 바로 넘기기보다, 우리 서비스에서 필요한 값만 골라 응답합니다.
        "data": {
            "id": external_data["id"],
            "title": external_data["title"],
            "body_preview": external_data["body"][:60],
        },
    }

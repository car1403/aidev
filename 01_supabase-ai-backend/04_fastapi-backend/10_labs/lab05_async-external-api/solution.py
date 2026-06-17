"""Lab 05 solution: async와 외부 API 구조."""

import asyncio

from fastapi import FastAPI


app = FastAPI(title="Lab 05 Async External API")


@app.get("/wait")
async def wait_api(seconds: int = 1):
    """비동기 대기 예제입니다."""

    await asyncio.sleep(seconds)
    return {"message": "done", "waited": seconds}


@app.get("/mock-external")
async def mock_external(keyword: str = "fastapi"):
    """외부 API 호출을 흉내 내는 예제입니다."""

    await asyncio.sleep(1)
    return {
        "source": "mock",
        "keyword": keyword,
        "result": f"{keyword} search result",
    }

"""Lab 05 starter: async와 외부 API 구조."""

import asyncio

from fastapi import FastAPI


app = FastAPI(title="Lab 05 Starter")


@app.get("/wait")
async def wait_api(seconds: int = 1):
    """TODO: asyncio.sleep으로 비동기 대기를 연습합니다."""

    await asyncio.sleep(seconds)
    return {"waited": seconds}

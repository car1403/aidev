"""async endpoint 예제.

async def는 오래 걸리는 I/O 작업을 기다리는 동안 서버가 다른 요청을 처리할 수 있게 해줍니다.
DB 조회, 외부 API 호출, 파일 읽기 같은 작업과 함께 자주 사용합니다.
"""

import asyncio

from fastapi import FastAPI


app = FastAPI(title="Async Endpoint Practice")


@app.get("/slow-task")
async def slow_task(seconds: int = 2):
    """일부러 기다리는 API입니다.

    time.sleep()이 아니라 asyncio.sleep()을 사용해야 이벤트 루프를 막지 않습니다.
    """

    await asyncio.sleep(seconds)

    return {
        "message": "slow task finished",
        "waited_seconds": seconds,
    }


@app.get("/parallel-tasks")
async def parallel_tasks():
    """여러 비동기 작업을 동시에 기다리는 예제입니다."""

    async def fetch_mock_data(name: str, seconds: int):
        await asyncio.sleep(seconds)
        return {"name": name, "seconds": seconds}

    # gather는 여러 async 작업을 동시에 실행하고 모두 끝날 때까지 기다립니다.
    results = await asyncio.gather(
        fetch_mock_data("profile", 1),
        fetch_mock_data("history", 2),
        fetch_mock_data("logs", 1),
    )

    return {"data": results}

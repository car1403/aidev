"""async endpoint 예제입니다.

이 파일은 async/await 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 서버 실행은 같은 폴더의 main.py를 사용합니다.

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

    # await는 "이 작업이 끝날 때까지 기다리되, 서버 전체를 멈추지는 말라"는 의미입니다.
    await asyncio.sleep(seconds)

    return {
        "message": "slow task finished",
        "waited_seconds": seconds,
    }


@app.get("/parallel-tasks")
async def parallel_tasks():
    """여러 비동기 작업을 동시에 기다리는 예제입니다."""

    async def fetch_mock_data(name: str, seconds: int):
        # 외부 API 호출처럼 시간이 걸리는 작업을 흉내 냅니다.
        await asyncio.sleep(seconds)
        return {"name": name, "seconds": seconds}

    # gather는 여러 async 작업을 동시에 실행하고 모두 끝날 때까지 기다립니다.
    results = await asyncio.gather(
        fetch_mock_data("profile", 1),
        fetch_mock_data("history", 2),
        fetch_mock_data("logs", 1),
    )

    return {"data": results}

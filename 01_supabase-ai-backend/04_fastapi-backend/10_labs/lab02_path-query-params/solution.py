"""Lab 02 solution: Path/Query Parameter."""

from fastapi import FastAPI, Query


app = FastAPI(title="Lab 02 Path Query Params")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """URL 경로에서 user_id를 받습니다."""

    return {
        "user_id": user_id,
        "message": f"user {user_id} selected",
    }


@app.get("/search")
def search(
    keyword: str = Query(default="", description="검색어"),
    limit: int = Query(default=5, ge=1, le=20, description="최대 결과 수"),
):
    """Query parameter로 검색 조건을 받습니다."""

    return {
        "keyword": keyword,
        "limit": limit,
        "message": f"searching for {keyword}",
    }

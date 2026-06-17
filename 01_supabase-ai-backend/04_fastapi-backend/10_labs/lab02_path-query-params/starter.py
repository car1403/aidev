"""Lab 02 starter: Path/Query Parameter."""

from fastapi import FastAPI, Query


app = FastAPI(title="Lab 02 Starter")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """TODO: user_id를 응답에 포함해 보세요."""

    return {"user_id": user_id}


@app.get("/search")
def search(keyword: str = Query(default="")):
    """TODO: keyword와 limit을 함께 받도록 확장해 보세요."""

    return {"keyword": keyword}

"""Path Parameter 예제.

이 파일은 Path Parameter 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 실행은 같은 폴더의 main.py를 사용합니다.

Path Parameter는 URL 경로 안에 들어가는 값입니다.

예:
    /users/1
    /courses/python

위 URL에서 `1`, `python` 같은 값이 path parameter입니다.
"""

from fastapi import FastAPI, HTTPException


app = FastAPI(title="Path Parameter Practice")


users = {
    1: {"id": 1, "name": "Alice", "role": "student"},
    2: {"id": 2, "name": "Bob", "role": "mentor"},
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """사용자 id로 한 명의 사용자를 조회합니다."""

    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return {"data": users[user_id]}


@app.get("/courses/{course_slug}/lessons/{lesson_no}")
def get_lesson(course_slug: str, lesson_no: int):
    """경로 안에서 여러 개의 값을 받을 수도 있습니다."""

    return {
        "course": course_slug,
        "lesson_no": lesson_no,
        "message": f"{course_slug} course lesson {lesson_no}",
    }

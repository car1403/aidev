"""Query Parameter 예제.

이 파일은 Query Parameter 개념을 나누어 읽기 위한 학습용 파일입니다.
실제 실행은 같은 폴더의 main.py를 사용합니다.

Query Parameter는 URL의 `?` 뒤에 붙는 검색 조건입니다.

예:
    /search?keyword=python&limit=5
"""

from fastapi import FastAPI, Query


app = FastAPI(title="Query Parameter Practice")


courses = [
    {"id": 1, "title": "Python Basic", "level": "beginner"},
    {"id": 2, "title": "FastAPI Backend", "level": "beginner"},
    {"id": 3, "title": "Supabase Integration", "level": "intermediate"},
    {"id": 4, "title": "LLM API Practice", "level": "intermediate"},
]


@app.get("/search")
def search_courses(
    keyword: str = Query(default="", description="강의 제목에서 찾을 검색어"),
    level: str | None = Query(default=None, description="beginner 또는 intermediate"),
    limit: int = Query(default=10, ge=1, le=20, description="최대 반환 개수"),
):
    """검색 조건에 맞는 강의 목록을 반환합니다."""

    result = courses

    if keyword:
        result = [
            course
            for course in result
            if keyword.lower() in course["title"].lower()
        ]

    if level:
        result = [course for course in result if course["level"] == level]

    return {
        "keyword": keyword,
        "level": level,
        "limit": limit,
        "count": len(result[:limit]),
        "data": result[:limit],
    }

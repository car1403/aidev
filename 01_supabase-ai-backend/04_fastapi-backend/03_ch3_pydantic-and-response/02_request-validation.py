"""요청 데이터 검증 예제.

잘못된 요청이 들어오면 FastAPI는 자동으로 422 응답을 반환합니다.
이 예제에서는 필수값, 문자열 길이, 숫자 범위, 목록 길이를 검증합니다.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Request Validation Practice")


class QuizSubmission(BaseModel):
    """퀴즈 제출 요청 데이터입니다."""

    student_name: str = Field(min_length=2, examples=["Alice"])
    quiz_id: int = Field(ge=1, examples=[1])
    answers: list[str] = Field(min_length=1, max_length=10, examples=[["A", "C", "B"]])
    study_minutes: int = Field(ge=0, le=600, examples=[45])


@app.post("/quiz-submissions")
def submit_quiz(submission: QuizSubmission):
    """퀴즈 제출 데이터를 검증하고 간단한 결과를 반환합니다."""

    return {
        "message": "submission accepted",
        "student": submission.student_name,
        "answer_count": len(submission.answers),
        "study_minutes": submission.study_minutes,
    }

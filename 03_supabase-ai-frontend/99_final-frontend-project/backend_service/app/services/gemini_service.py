from fastapi import HTTPException

from app.core.config import GEMINI_API_KEY, GEMINI_MODEL


def generate_ai_answer(user_message: str) -> dict[str, str | bool]:
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY가 설정되어 있지 않습니다.")

    try:
        from google import genai

        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"초보자에게 친절한 한국어 답변을 작성하세요.\n\n질문: {user_message}",
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Gemini API 호출 실패: {exc}") from exc

    return {
        "answer": response.text or "응답 내용이 비어 있습니다.",
        "provider": "gemini",
        "model": GEMINI_MODEL,
        "actual_api_called": True,
    }

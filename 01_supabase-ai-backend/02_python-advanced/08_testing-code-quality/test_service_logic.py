"""pytest로 서비스 함수를 검증하는 예제입니다."""

import pytest

from service_logic import build_chat_response, normalize_question, validate_question


def test_normalize_question_removes_spaces() -> None:
    """질문 앞뒤 공백이 제거되는지 확인합니다."""

    assert normalize_question("  Supabase란?  ") == "Supabase란?"


def test_validate_question_rejects_empty_text() -> None:
    """빈 질문이면 ValueError가 발생해야 합니다."""

    with pytest.raises(ValueError):
        validate_question("   ")


def test_build_chat_response_has_required_keys() -> None:
    """응답 dict에 question과 answer key가 있는지 확인합니다."""

    response = build_chat_response("FastAPI란?")

    assert response["question"] == "FastAPI란?"
    assert "answer" in response
    assert response["answer"] != ""

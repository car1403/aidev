"""챗봇 요청/응답 관리 미니 프로젝트 테스트입니다."""

import pytest

from chat_response_manager import (
    ChatRecord,
    build_chat_record,
    load_records,
    normalize_question,
    save_records,
    search_records,
    stream_answer,
    validate_question,
)


def test_normalize_question_removes_spaces() -> None:
    """질문 앞뒤 공백이 제거되는지 확인합니다."""

    assert normalize_question("  FastAPI란?  ") == "FastAPI란?"


def test_validate_question_rejects_empty_text() -> None:
    """빈 질문이면 ValueError가 발생해야 합니다."""

    with pytest.raises(ValueError):
        validate_question("   ")


def test_build_chat_record_has_required_fields() -> None:
    """질문을 ChatRecord 객체로 만들 수 있는지 확인합니다."""

    record = build_chat_record("JSON은 왜 사용하나요?", record_id=1)

    assert record.record_id == 1
    assert record.question == "JSON은 왜 사용하나요?"
    assert record.answer != ""
    assert record.created_at != ""


def test_save_and_load_records(tmp_path) -> None:
    """JSON 파일로 저장한 뒤 다시 읽을 수 있는지 확인합니다."""

    file_path = tmp_path / "chat_records.json"
    records = [
        ChatRecord(
            record_id=1,
            question="FastAPI란?",
            answer="FastAPI는 API 서버를 만들 때 사용합니다.",
            created_at="2026-06-22T00:00:00+00:00",
        )
    ]

    save_records(records, file_path=file_path)
    loaded_records = load_records(file_path=file_path)

    assert len(loaded_records) == 1
    assert loaded_records[0].question == "FastAPI란?"


def test_search_records_finds_keyword() -> None:
    """질문에 키워드가 포함된 기록만 검색되는지 확인합니다."""

    records = [
        ChatRecord(1, "FastAPI란?", "API 서버 도구입니다.", "2026-06-22T00:00:00+00:00"),
        ChatRecord(2, "JSON이란?", "데이터 형식입니다.", "2026-06-22T00:00:01+00:00"),
    ]

    results = search_records(records, "JSON")

    assert len(results) == 1
    assert results[0].question == "JSON이란?"


def test_stream_answer_returns_words() -> None:
    """yield로 답변 단어를 하나씩 받을 수 있는지 확인합니다."""

    words = list(stream_answer("AI 응답을 나누어 출력합니다"))

    assert words == ["AI", "응답을", "나누어", "출력합니다"]

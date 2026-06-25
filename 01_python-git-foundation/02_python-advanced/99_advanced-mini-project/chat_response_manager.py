"""챗봇 요청/응답 관리 CLI 미니 프로젝트입니다.

이 파일은 실제 AI API를 호출하지 않습니다.
대신 질문을 정리하고, 검증하고, 임시 답변을 만들고, JSON 파일에 저장하는 흐름을 연습합니다.
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from json import JSONDecodeError
from pathlib import Path


# 저장 파일 위치입니다.
# C:\aidev\01_python-git-foundation 에서 실행하면 data/chat_records.json에 저장됩니다.
DATA_DIR = Path("data")
CHAT_LOG_FILE = DATA_DIR / "chat_records.json"


@dataclass
class ChatRecord:
    """질문과 답변 기록 한 건을 표현합니다."""

    record_id: int
    question: str
    answer: str
    created_at: str


def normalize_question(question: str) -> str:
    """질문 앞뒤 공백을 제거합니다."""

    return question.strip()


def validate_question(question: str) -> None:
    """질문이 비어 있는지 검사합니다."""

    if normalize_question(question) == "":
        raise ValueError("질문은 비워둘 수 없습니다.")


def create_temporary_answer(question: str) -> str:
    """연습용 답변을 생성합니다.

    실제 과정에서는 이 부분이 AI 모델 API 호출 코드로 바뀔 수 있습니다.
    지금은 Python 구조를 배우는 단계이므로 고정된 규칙으로 답변을 만듭니다.
    """

    if "FastAPI" in question:
        return "FastAPI는 Python으로 API 서버를 만들 때 사용하는 웹 프레임워크입니다."

    if "JSON" in question:
        return "JSON은 API 응답과 데이터 저장에서 자주 사용하는 데이터 형식입니다."

    return "좋은 질문입니다. 이후 AI API 단원에서 실제 모델 응답으로 바꿔볼 수 있습니다."


def build_chat_record(question: str, record_id: int) -> ChatRecord:
    """질문을 받아 ChatRecord 객체를 만듭니다."""

    clean_question = normalize_question(question)
    validate_question(clean_question)

    answer = create_temporary_answer(clean_question)
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    return ChatRecord(
        record_id=record_id,
        question=clean_question,
        answer=answer,
        created_at=created_at,
    )


def load_records(file_path: Path = CHAT_LOG_FILE) -> list[ChatRecord]:
    """JSON 파일에서 기존 질문/답변 기록을 읽어옵니다."""

    if not file_path.exists():
        return []

    try:
        raw_records = json.loads(file_path.read_text(encoding="utf-8"))
    except JSONDecodeError:
        print("저장 파일의 JSON 형식이 올바르지 않아 빈 목록으로 시작합니다.")
        return []

    return [ChatRecord(**item) for item in raw_records]


def save_records(records: list[ChatRecord], file_path: Path = CHAT_LOG_FILE) -> None:
    """질문/답변 기록을 JSON 파일에 저장합니다."""

    file_path.parent.mkdir(exist_ok=True)

    data = [asdict(record) for record in records]
    json_text = json.dumps(data, ensure_ascii=False, indent=2)

    file_path.write_text(json_text, encoding="utf-8")


def show_records(records: list[ChatRecord]) -> None:
    """저장된 질문/답변 목록을 출력합니다."""

    if not records:
        print("저장된 질문이 없습니다.")
        return

    for record in records:
        print(f"\n[{record.record_id}] {record.question}")
        print(f"답변: {record.answer}")
        print(f"생성 시각: {record.created_at}")


def search_records(records: list[ChatRecord], keyword: str) -> list[ChatRecord]:
    """질문에 특정 키워드가 포함된 기록만 찾습니다."""

    clean_keyword = keyword.strip()

    if clean_keyword == "":
        return []

    return [record for record in records if clean_keyword in record.question]


def stream_answer(answer: str):
    """답변을 단어 단위로 하나씩 내보냅니다."""

    for word in answer.split():
        yield word


def add_record(records: list[ChatRecord]) -> None:
    """사용자에게 질문을 입력받고 기록에 추가합니다."""

    question = input("질문을 입력하세요: ")
    next_id = len(records) + 1

    record = build_chat_record(question=question, record_id=next_id)
    records.append(record)
    save_records(records)

    print("질문과 답변을 저장했습니다.")
    print("답변:", record.answer)


def search_menu(records: list[ChatRecord]) -> None:
    """검색어를 입력받아 질문 기록을 검색합니다."""

    keyword = input("검색어를 입력하세요: ")
    results = search_records(records, keyword)

    if not results:
        print("검색 결과가 없습니다.")
        return

    show_records(results)


def stream_menu(records: list[ChatRecord]) -> None:
    """가장 최근 답변을 단어 단위로 출력합니다."""

    if not records:
        print("먼저 질문을 추가해 주세요.")
        return

    latest_record = records[-1]

    print("최근 답변을 단어 단위로 출력합니다.")
    for word in stream_answer(latest_record.answer):
        print(word)


def main() -> None:
    """챗봇 요청/응답 관리 프로그램의 시작점입니다."""

    records = load_records()

    while True:
        print("\n[챗봇 요청/응답 관리]")
        print("1. 질문 추가")
        print("2. 저장된 질문 목록 보기")
        print("3. 키워드 검색")
        print("4. 답변 스트리밍 흉내 보기")
        print("5. 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            try:
                add_record(records)
            except ValueError as error:
                print("오류:", error)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            search_menu(records)
        elif choice == "4":
            stream_menu(records)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1, 2, 3, 4, 5 중에서 선택하세요.")


if __name__ == "__main__":
    main()

"""백엔드에서 자주 사용하는 Service class 구조 예제입니다."""


class LearningNoteService:
    """학습 노트를 관리하는 서비스 클래스입니다."""

    def __init__(self) -> None:
        """서비스가 사용할 데이터를 준비합니다."""

        # 실제 서비스에서는 이 부분이 Supabase 테이블이나 데이터베이스가 될 수 있습니다.
        # 여기서는 처음 배우는 단계이므로 리스트로 간단히 흉내 냅니다.
        self.notes: list[dict[str, str]] = []

    def add_note(self, title: str, content: str) -> dict[str, str]:
        """학습 노트를 추가합니다."""

        # 새 노트를 dict로 만듭니다.
        note = {
            "title": title,
            "content": content,
        }

        # 서비스가 관리하는 목록에 노트를 추가합니다.
        self.notes.append(note)

        # 추가한 노트를 반환합니다.
        return note

    def list_notes(self) -> list[dict[str, str]]:
        """저장된 학습 노트 목록을 반환합니다."""

        # 내부 리스트를 그대로 반환합니다.
        return self.notes


# 서비스 객체를 만듭니다.
service = LearningNoteService()

# 서비스 객체의 메서드를 사용해 데이터를 추가합니다.
service.add_note("FastAPI", "API 서버를 쉽게 만들 수 있는 프레임워크입니다.")
service.add_note("Supabase", "PostgreSQL 기반 백엔드 서비스를 빠르게 사용할 수 있습니다.")

# 서비스 객체가 관리하는 데이터를 출력합니다.
print("저장된 노트 목록:")
for note in service.list_notes():
    print("-", note["title"], ":", note["content"])

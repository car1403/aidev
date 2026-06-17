"""클래스와 객체 기초 예제입니다."""


class TodoItem:
    """할 일 하나를 표현하는 클래스입니다."""

    def __init__(self, title: str) -> None:
        self.title = title
        self.done = False

    def complete(self) -> None:
        """할 일을 완료 상태로 바꿉니다."""

        self.done = True

    def label(self) -> str:
        """화면에 보여줄 문자열을 반환합니다."""

        status = "완료" if self.done else "진행중"
        return f"[{status}] {self.title}"


todo = TodoItem("클래스 공부")
print(todo.label())
todo.complete()
print(todo.label())

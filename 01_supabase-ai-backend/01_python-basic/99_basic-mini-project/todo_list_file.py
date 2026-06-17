"""파일 저장형 할 일 목록 미니 프로젝트입니다.

이 파일은 Python 기초 문법을 모아 만든 작은 프로그램입니다.

사용하는 개념:

1. 리스트로 여러 할 일을 저장하기
2. 함수로 기능을 나누기
3. while 반복문으로 메뉴를 계속 보여주기
4. input()으로 사용자 선택 받기
5. JSON 파일로 데이터를 저장하고 다시 읽기
"""

import json
from pathlib import Path

# 데이터를 저장할 폴더와 파일 경로를 상수로 정의합니다.
# 대문자 변수명은 보통 "프로그램 전체에서 고정해서 쓰는 값"이라는 의미로 사용합니다.
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
TODO_FILE = DATA_DIR / "todos.json"


def load_todos() -> list[str]:
    """파일에서 할 일 목록을 읽어옵니다.

    반환값:
        파일에 저장된 할 일 목록입니다.
        파일이 아직 없으면 빈 리스트를 반환합니다.
    """

    # 프로그램을 처음 실행하면 todos.json 파일이 아직 없을 수 있습니다.
    # exists()로 파일이 있는지 먼저 확인합니다.
    if not TODO_FILE.exists():
        return []

    # 파일 내용은 JSON 문자열이므로 json.loads()로 Python 리스트로 바꿉니다.
    return json.loads(TODO_FILE.read_text(encoding="utf-8"))


def save_todos(todos: list[str]) -> None:
    """할 일 목록을 파일에 저장합니다.

    매개변수:
        todos: 저장할 할 일 문자열 리스트입니다.

    반환값:
        파일 저장만 수행하므로 반환값은 없습니다.
    """

    # json.dumps()는 Python 리스트를 JSON 문자열로 바꿉니다.
    # ensure_ascii=False는 한글이 그대로 보이게 저장합니다.
    # indent=2는 파일을 사람이 읽기 좋게 정렬합니다.
    TODO_FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")


def show_todos(todos: list[str]) -> None:
    """현재 할 일 목록을 출력합니다.

    매개변수:
        todos: 화면에 보여 줄 할 일 목록입니다.
    """

    # 리스트가 비어 있으면 False처럼 판단됩니다.
    # not todos는 "할 일이 하나도 없다"는 뜻으로 이해하면 됩니다.
    if not todos:
        print("등록된 할 일이 없습니다.")
        return

    # enumerate()로 할 일마다 번호를 붙입니다.
    # start=1을 사용해 1번부터 보여줍니다.
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")


def main() -> None:
    """할 일 목록 프로그램의 시작점입니다.

    프로그램의 전체 흐름을 담당합니다.
    파일에서 기존 할 일을 읽고, 사용자가 종료를 선택할 때까지 메뉴를 반복합니다.
    """

    # 프로그램 시작 시 파일에 저장된 할 일 목록을 읽어옵니다.
    todos = load_todos()

    # True는 항상 참이므로 사용자가 종료를 선택할 때까지 계속 반복됩니다.
    while True:
        print("\n[할 일 목록]")
        print("1. 보기")
        print("2. 추가")
        print("3. 종료")

        # 사용자가 입력한 메뉴 번호는 문자열로 들어옵니다.
        # 그래서 숫자 1이 아니라 문자열 "1"과 비교합니다.
        choice = input("선택: ")

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            todo = input("추가할 할 일: ")

            # 새 할 일을 리스트 끝에 추가합니다.
            todos.append(todo)

            # 추가한 내용을 파일에도 저장해야 다음 실행 때 다시 볼 수 있습니다.
            save_todos(todos)
            print("저장했습니다.")
        elif choice == "3":
            print("프로그램을 종료합니다.")

            # break는 while 반복문을 끝냅니다.
            break
        else:
            print("1, 2, 3 중에서 선택하세요.")


# 이 파일을 직접 실행할 때만 main()을 호출합니다.
# 나중에 다른 파일에서 이 파일을 import할 경우에는 main()이 자동 실행되지 않습니다.
if __name__ == "__main__":
    main()

"""파일 저장형 학습 기록 관리 미니 프로젝트입니다.

이 파일은 Python 기초 문법을 모아 만든 작은 프로그램입니다.

사용하는 개념:

1. list 안에 dict를 넣어 여러 학습 기록 저장하기
2. 함수로 기능을 나누기
3. while True로 메뉴를 계속 보여주기
4. input()으로 사용자 선택 받기
5. if / elif / else로 메뉴 처리하기
6. JSON 파일로 데이터를 저장하고 다시 읽기
"""

# json은 Python 자료구조를 JSON 파일로 저장하거나,
# JSON 파일을 다시 Python 자료구조로 읽을 때 사용합니다.
import json

# Path는 파일과 폴더 경로를 다룰 때 사용합니다.
from pathlib import Path

# 데이터를 저장할 폴더 경로입니다.
DATA_DIR = Path("data")

# data 폴더가 없으면 새로 만듭니다.
DATA_DIR.mkdir(exist_ok=True)

# 학습 기록을 저장할 JSON 파일 경로입니다.
RECORD_FILE = DATA_DIR / "learning_records.json"


def add_record(records):
    """학습 기록을 하나 추가합니다.

    매개변수:
        records: 학습 기록 dict들이 들어 있는 list입니다.
    """

    # 학습 제목을 입력받습니다.
    title = input("학습 제목을 입력하세요: ")

    # 학습 시간을 문자열로 입력받습니다.
    minutes_text = input("학습 시간(분)을 입력하세요: ")

    # 숫자 계산을 위해 문자열을 정수로 바꿉니다.
    minutes = int(minutes_text)

    # 완료 여부를 입력받습니다.
    done_text = input("완료했나요? (y/n): ")

    # y 또는 Y를 입력하면 True, 그 외에는 False로 저장합니다.
    done = done_text.strip().lower() == "y"

    # 학습 기록 하나를 dict로 만듭니다.
    record = {
        "title": title,
        "minutes": minutes,
        "done": done,
    }

    # records list에 새 기록을 추가합니다.
    records.append(record)

    print("학습 기록을 추가했습니다.")


def print_records(records):
    """전체 학습 기록을 출력합니다."""

    # 기록이 없으면 안내 문장을 출력하고 함수를 종료합니다.
    if not records:
        print("등록된 학습 기록이 없습니다.")
        return

    # enumerate()로 번호를 붙여 출력합니다.
    for index, record in enumerate(records, start=1):
        print_record(index, record)


def print_done_records(records):
    """완료한 학습 기록만 출력합니다."""

    # 완료한 기록이 하나라도 있는지 확인하기 위한 변수입니다.
    found = False

    for index, record in enumerate(records, start=1):
        # done 값이 True인 기록만 출력합니다.
        if record["done"]:
            print_record(index, record)
            found = True

    # 반복문이 끝났는데 완료 기록이 없으면 안내 문장을 출력합니다.
    if not found:
        print("완료한 학습 기록이 없습니다.")


def print_record(index, record):
    """학습 기록 하나를 보기 좋게 출력합니다."""

    # done 값에 따라 화면에 보여 줄 문장을 정합니다.
    status = "완료" if record["done"] else "진행 중"

    print(f"{index}. {record['title']}")
    print(f"   시간: {record['minutes']}분")
    print(f"   상태: {status}")


def calculate_total_minutes(records):
    """전체 학습 시간을 계산합니다."""

    total = 0

    # records 안의 각 record에서 minutes 값을 꺼내 더합니다.
    for record in records:
        total += record["minutes"]

    return total


def save_records(records):
    """학습 기록을 JSON 파일로 저장합니다."""

    # json.dumps()는 Python list/dict를 JSON 문자열로 바꿉니다.
    # ensure_ascii=False는 한글을 그대로 저장하게 합니다.
    # indent=2는 파일을 사람이 읽기 좋게 들여쓰기합니다.
    json_text = json.dumps(records, ensure_ascii=False, indent=2)

    # JSON 문자열을 파일에 저장합니다.
    RECORD_FILE.write_text(json_text, encoding="utf-8")

    print("학습 기록을 저장했습니다:", RECORD_FILE)


def load_records():
    """JSON 파일에서 학습 기록을 읽어옵니다."""

    # 파일이 아직 없으면 빈 list를 반환합니다.
    if not RECORD_FILE.exists():
        print("저장된 파일이 없습니다. 빈 목록으로 시작합니다.")
        return []

    # 파일 내용을 문자열로 읽습니다.
    json_text = RECORD_FILE.read_text(encoding="utf-8")

    # JSON 문자열을 Python list로 바꿉니다.
    records = json.loads(json_text)

    print("학습 기록을 불러왔습니다:", RECORD_FILE)
    return records


def print_menu():
    """메뉴를 출력합니다."""

    print("\n[학습 기록 관리]")
    print("1. 학습 기록 추가")
    print("2. 전체 학습 기록 보기")
    print("3. 완료한 학습만 보기")
    print("4. 총 학습 시간 보기")
    print("5. JSON 파일로 저장")
    print("6. JSON 파일에서 읽기")
    print("q. 종료")


def main():
    """프로그램의 전체 흐름을 담당합니다."""

    # 프로그램이 시작될 때는 빈 list로 시작합니다.
    records = []

    # 사용자가 q를 선택할 때까지 계속 반복합니다.
    while True:
        print_menu()

        # 메뉴 선택값은 문자열로 입력됩니다.
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_record(records)

        elif choice == "2":
            print_records(records)

        elif choice == "3":
            print_done_records(records)

        elif choice == "4":
            total = calculate_total_minutes(records)
            print("총 학습 시간:", total, "분")

        elif choice == "5":
            save_records(records)

        elif choice == "6":
            records = load_records()

        elif choice.strip().lower() == "q":
            print("프로그램을 종료합니다.")
            break

        else:
            print("알 수 없는 메뉴입니다. 다시 선택하세요.")


# 이 파일을 직접 실행할 때만 main()을 호출합니다.
# 다른 파일에서 import할 때 자동 실행되는 것을 막기 위한 Python 관용구입니다.
if __name__ == "__main__":
    main()

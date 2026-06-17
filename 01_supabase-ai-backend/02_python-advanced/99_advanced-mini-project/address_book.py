"""JSON 기반 CLI 주소록 미니 프로젝트입니다."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
ADDRESS_FILE = DATA_DIR / "address_book.json"


@dataclass
class Contact:
    """연락처 한 명을 표현합니다."""

    name: str
    phone: str
    email: str


def load_contacts() -> list[Contact]:
    """JSON 파일에서 연락처 목록을 읽어옵니다."""

    if not ADDRESS_FILE.exists():
        return []

    raw_contacts = json.loads(ADDRESS_FILE.read_text(encoding="utf-8"))
    return [Contact(**item) for item in raw_contacts]


def save_contacts(contacts: list[Contact]) -> None:
    """연락처 목록을 JSON 파일에 저장합니다."""

    data = [asdict(contact) for contact in contacts]
    ADDRESS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def show_contacts(contacts: list[Contact]) -> None:
    """연락처 목록을 출력합니다."""

    if not contacts:
        print("등록된 연락처가 없습니다.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact.name} / {contact.phone} / {contact.email}")


def add_contact(contacts: list[Contact]) -> None:
    """새 연락처를 입력받아 목록에 추가합니다."""

    name = input("이름: ").strip()
    phone = input("전화번호: ").strip()
    email = input("이메일: ").strip()

    if not name or not phone:
        raise ValueError("이름과 전화번호는 필수입니다.")

    contacts.append(Contact(name=name, phone=phone, email=email))
    save_contacts(contacts)
    print("연락처를 저장했습니다.")


def main() -> None:
    """주소록 프로그램의 시작점입니다."""

    contacts = load_contacts()

    while True:
        print("\n[주소록]")
        print("1. 목록 보기")
        print("2. 연락처 추가")
        print("3. 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            try:
                add_contact(contacts)
            except ValueError as error:
                print("오류:", error)
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1, 2, 3 중에서 선택하세요.")


if __name__ == "__main__":
    main()

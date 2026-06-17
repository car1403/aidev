"""샘플 프로젝트 시작점입니다."""

from app.services import build_message


def main() -> None:
    print(build_message("Jean"))


if __name__ == "__main__":
    main()

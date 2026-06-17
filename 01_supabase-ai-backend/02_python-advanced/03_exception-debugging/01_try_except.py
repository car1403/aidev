"""try/except 예제입니다."""


def parse_age(text: str) -> int:
    """문자열을 나이 숫자로 변환합니다."""

    try:
        age = int(text)
    except ValueError:
        print("숫자로 변환할 수 없습니다.")
        return 0
    else:
        return age
    finally:
        print("parse_age 실행 완료")


print(parse_age("30"))
print(parse_age("abc"))

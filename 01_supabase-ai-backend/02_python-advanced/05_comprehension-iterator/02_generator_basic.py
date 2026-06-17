"""generator 기초 예제입니다."""


def count_up_to(limit: int):
    """1부터 limit까지 값을 하나씩 생성합니다."""

    number = 1
    while number <= limit:
        yield number
        number += 1


for value in count_up_to(5):
    print(value)

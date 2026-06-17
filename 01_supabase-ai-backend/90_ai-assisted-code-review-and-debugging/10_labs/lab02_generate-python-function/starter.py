"""Lab 02 - Python 함수 생성 요청 starter.

이 파일은 Codex에게 명확한 요구사항을 전달하고,
생성된 함수가 요구사항을 만족하는지 학생이 직접 검증하는 실습용입니다.
"""


def calculate_average(scores: list[float]) -> float:
    """점수 목록의 평균을 반환합니다.

    실습 목표:
    1. Codex에게 이 함수 구현을 요청합니다.
    2. 빈 리스트는 0을 반환하도록 조건을 명확히 전달합니다.
    3. 생성된 코드를 그대로 믿지 말고 아래 테스트를 직접 실행합니다.
    """

    if not scores:
        return 0

    return sum(scores) / len(scores)


test_cases = [
    [90, 80, 70],
    [100],
    [],
]

for test_case in test_cases:
    print(f"{test_case} -> {calculate_average(test_case)}")

"""외부 API 없이 동기(sync) 흐름만 이해하는 예제입니다.

이 예제는 네트워크를 사용하지 않습니다.
대신 time.sleep으로 "오래 걸리는 작업"을 흉내 냅니다.

동기 방식에서는 작업 하나가 끝나야 다음 작업을 시작합니다.
"""

import time


def print_step(message: str) -> None:
    """동기 예제의 실행 단계를 보기 좋게 출력합니다."""

    # 같은 형식으로 로그를 찍으면 실행 순서를 눈으로 따라가기 쉽습니다.
    # [SYNC-FLOW]라는 접두어는 이 파일이 동기 흐름 예제라는 것을 표시합니다.
    print(f"[SYNC-FLOW] {message}")


def make_coffee(order_name: str, seconds: int) -> str:
    """커피 한 잔을 만드는 데 시간이 걸린다고 가정합니다.

    time.sleep(seconds)는 현재 프로그램을 지정한 초만큼 멈춥니다.
    이 시간 동안 다음 주문은 시작되지 않습니다.
    """

    # order_name은 주문 이름입니다. 예: "아메리카노"
    # seconds는 작업이 걸리는 시간입니다. 예: 2초
    print_step(f"{order_name}: 주문을 받았습니다.")
    print_step(f"{order_name}: 만들기 시작합니다. {seconds}초 동안 여기서 기다립니다.")

    # 동기 방식의 핵심입니다.
    # 이 줄이 끝나기 전까지 다음 줄도, 다음 주문도 실행되지 않습니다.
    # 즉, 프로그램은 여기에서 실제로 멈춘 것처럼 기다립니다.
    time.sleep(seconds)

    # sleep이 끝난 뒤에야 이 줄이 실행됩니다.
    print_step(f"{order_name}: 만들기가 끝났습니다.")

    # 함수가 처리 결과 문자열을 호출한 쪽으로 돌려줍니다.
    return f"{order_name} 완료"


def main() -> None:
    """동기 방식으로 커피 주문 3개를 순서대로 처리합니다."""

    print_step("0. 프로그램을 시작합니다.")

    # perf_counter는 시간 측정에 적합한 값을 반환합니다.
    # 시작 시각을 저장해 두었다가 마지막에 빼면 전체 실행 시간을 계산할 수 있습니다.
    started_at = time.perf_counter()

    # 첫 번째 주문을 처리합니다.
    # make_coffee 안에서 time.sleep(2)이 실행되므로 2초 동안 다음 줄로 넘어가지 않습니다.
    result_1 = make_coffee("아메리카노", 2)
    print_step(f"결과 확인: {result_1}")

    # 두 번째 주문은 첫 번째 주문이 완전히 끝난 뒤에야 시작됩니다.
    result_2 = make_coffee("라떼", 2)
    print_step(f"결과 확인: {result_2}")

    # 세 번째 주문도 앞의 두 주문이 모두 끝난 뒤에 시작됩니다.
    result_3 = make_coffee("모카", 2)
    print_step(f"결과 확인: {result_3}")

    # 현재 시각에서 시작 시각을 빼서 전체 걸린 시간을 구합니다.
    # 주문 3개가 각각 2초씩 걸리므로 총 약 6초가 나오는 것이 정상입니다.
    elapsed = time.perf_counter() - started_at
    print_step(f"총 걸린 시간: 약 {elapsed:.1f}초")
    print_step("동기 방식은 작업을 하나씩 끝낸 뒤 다음 작업을 시작합니다.")


# 이 파일을 직접 실행할 때만 main()을 호출합니다.
# 다른 파일에서 import할 때는 자동으로 실행되지 않게 하기 위한 Python의 관용적인 구조입니다.
if __name__ == "__main__":
    main()

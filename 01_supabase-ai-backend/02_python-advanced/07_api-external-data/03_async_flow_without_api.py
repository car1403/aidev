"""외부 API 없이 비동기(async/await) 흐름만 이해하는 예제입니다.

이 예제는 네트워크를 사용하지 않습니다.
대신 asyncio.sleep으로 "오래 걸리는 작업"을 흉내 냅니다.

비동기 방식에서는 기다리는 시간이 생길 때 다른 작업도 함께 시작할 수 있습니다.
"""

import asyncio
import time


def print_step(message: str) -> None:
    """비동기 예제의 실행 단계를 보기 좋게 출력합니다."""

    # 같은 형식으로 로그를 찍어 두면 여러 작업이 섞여 실행될 때도 흐름을 확인하기 쉽습니다.
    print(f"[ASYNC-FLOW] {message}")


async def make_coffee(order_name: str, seconds: int) -> str:
    """커피 한 잔을 비동기 방식으로 만든다고 가정합니다.

    asyncio.sleep(seconds)는 time.sleep과 다르게 이벤트 루프에 제어권을 돌려줍니다.
    그래서 이 주문이 기다리는 동안 다른 주문도 시작될 수 있습니다.
    """

    # async def로 만든 함수는 coroutine 함수입니다.
    # 일반 함수처럼 보이지만, 내부에서 await를 만나면 잠시 멈추고 다른 작업에 순서를 넘길 수 있습니다.
    print_step(f"{order_name}: 주문을 받았습니다.")
    print_step(f"{order_name}: 만들기 시작합니다. await 지점에서 {seconds}초 기다립니다.")

    # 비동기 방식의 핵심입니다.
    # 이 작업은 기다리지만, 이벤트 루프는 다른 coroutine도 실행할 수 있습니다.
    # time.sleep과 달리 프로그램 전체를 막아두지 않습니다.
    await asyncio.sleep(seconds)

    # 각 주문은 자신의 기다림이 끝나면 다시 이 위치부터 실행됩니다.
    print_step(f"{order_name}: 만들기가 끝났습니다.")

    # 비동기 함수도 return 값을 가질 수 있습니다.
    # 이 값은 await 또는 asyncio.gather를 통해 받을 수 있습니다.
    return f"{order_name} 완료"


async def main() -> None:
    """비동기 방식으로 커피 주문 3개를 동시에 진행합니다."""

    print_step("0. async main 함수를 시작합니다.")

    # 동기 예제와 비교하기 위해 전체 실행 시간을 측정합니다.
    started_at = time.perf_counter()

    print_step("1. 주문 3개를 coroutine으로 준비합니다. 아직 모두 끝난 것은 아닙니다.")

    # make_coffee(...)를 호출하면 coroutine 객체가 만들어집니다.
    # 중요한 점은 이 시점에 2초 기다리는 작업이 바로 끝난 것이 아니라는 점입니다.
    # 실제 실행은 아래에서 asyncio.gather를 await할 때 이벤트 루프가 관리합니다.
    orders = [
        make_coffee("아메리카노", 2),
        make_coffee("라떼", 2),
        make_coffee("모카", 2),
    ]

    print_step("2. asyncio.gather를 await합니다. 이제 주문 3개가 함께 진행됩니다.")

    # asyncio.gather는 여러 coroutine을 동시에 실행하고,
    # 모든 결과를 리스트 형태로 모아서 반환합니다.
    # 주문 3개가 각각 2초 걸리더라도 동시에 기다리므로 전체 시간은 약 2초에 가깝습니다.
    results = await asyncio.gather(*orders)

    print_step("3. 모든 주문이 끝났습니다. 결과를 출력합니다.")

    # gather가 반환한 결과 리스트를 하나씩 출력합니다.
    for result in results:
        print_step(f"결과 확인: {result}")

    # 비동기 방식의 실행 시간을 동기 방식과 비교해 봅니다.
    elapsed = time.perf_counter() - started_at
    print_step(f"총 걸린 시간: 약 {elapsed:.1f}초")
    print_step("비동기 방식은 기다리는 시간이 많은 작업을 함께 진행할 수 있습니다.")


# 이 파일을 직접 실행했을 때만 아래 코드가 실행됩니다.
if __name__ == "__main__":
    print_step("프로그램 시작. asyncio.run이 이벤트 루프를 만듭니다.")

    # asyncio.run은 비동기 main 함수를 실행하기 위해 이벤트 루프를 만들고,
    # main 함수가 끝나면 이벤트 루프를 정리합니다.
    asyncio.run(main())
    print_step("프로그램 종료.")

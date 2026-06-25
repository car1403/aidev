"""async/await로 여러 도시의 날씨 API를 동시에 호출하는 예제입니다.

비동기 처리는 CPU 계산을 빠르게 만드는 기술이 아닙니다.
네트워크 요청, 파일 입출력, 데이터베이스 요청처럼 기다리는 시간이 많은 작업을
효율적으로 처리하기 위한 방식입니다.
"""

import asyncio
import json
from typing import Any

import httpx


# Open-Meteo 날씨 API 주소입니다.
# 여러 도시를 조회하더라도 같은 URL에 좌표 값만 다르게 전달합니다.
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# 동시에 조회할 도시 목록입니다.
# 각 dict는 도시명, 위도, 경도를 가지고 있습니다.
# 실제 API 호출에서는 name은 사용하지 않고, 사람이 보기 좋게 출력할 때 사용합니다.
CITIES = [
    {"name": "서울", "latitude": 37.5665, "longitude": 126.9780},
    {"name": "부산", "latitude": 35.1796, "longitude": 129.0756},
    {"name": "제주", "latitude": 33.4996, "longitude": 126.5312},
]


def print_step(message: str) -> None:
    """실행 흐름을 눈으로 확인하기 위해 단계 메시지를 출력합니다."""

    # 여러 도시 요청이 동시에 진행되면 출력 순서가 섞일 수 있습니다.
    # 그래서 [ASYNC] 접두어와 도시명을 함께 출력해 흐름을 추적합니다.
    print(f"[ASYNC] {message}")


async def fetch_weather(client: httpx.AsyncClient, city: dict[str, Any]) -> dict[str, Any]:
    """도시 하나의 날씨를 비동기 방식으로 가져옵니다.

    async def로 만든 함수는 바로 실행 결과를 반환하지 않고 coroutine을 만듭니다.
    실제 실행은 await를 만났을 때 이벤트 루프가 관리합니다.
    """

    # city dict에서 도시 이름을 꺼냅니다.
    # 로그와 최종 출력에서 어떤 도시의 결과인지 구분하기 위해 사용합니다.
    city_name = city["name"]
    print_step(f"{city_name}: fetch_weather 함수가 시작되었습니다.")

    # API에 전달할 query parameter입니다.
    # 도시마다 latitude, longitude 값만 달라지고 나머지 요청 구조는 같습니다.
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "Asia/Seoul",
    }

    print_step(f"{city_name}: 요청 파라미터를 만들었습니다.")
    print_step(f"{city_name}: await client.get 실행. 이 요청은 기다리지만, 이벤트 루프는 다른 도시 요청도 처리할 수 있습니다.")

    # await는 "응답이 올 때까지 이 작업은 기다리되, 이벤트 루프는 다른 작업을 처리해도 된다"는 뜻입니다.
    # 예를 들어 서울 요청이 응답을 기다리는 동안 부산, 제주 요청도 함께 진행될 수 있습니다.
    response = await client.get(OPEN_METEO_URL, params=params)

    print_step(f"{city_name}: API 응답을 받았습니다.")

    # HTTP 상태 코드가 4xx/5xx이면 예외를 발생시킵니다.
    # 이 예외는 asyncio.gather(..., return_exceptions=True)에 의해 결과 리스트에 담길 수 있습니다.
    response.raise_for_status()

    # JSON 응답을 Python dict로 변환합니다.
    data = response.json()

    # API 원본 응답에는 우리가 지정한 한글 도시명이 없기 때문에,
    # 출력하기 쉽도록 city_name key를 직접 추가합니다.
    data["city_name"] = city_name
    print_step(f"{city_name}: JSON을 dict로 바꾸고 결과를 반환합니다.")
    return data


def format_weather_summary(data: dict[str, Any]) -> str:
    """도시별 날씨 응답을 한 줄 요약으로 바꿉니다."""

    # fetch_weather에서 직접 추가한 city_name을 꺼냅니다.
    city_name = data["city_name"]

    # current에는 현재 날씨 값이, current_units에는 각 값의 단위가 들어 있습니다.
    current = data["current"]
    units = data["current_units"]

    # 필요한 값만 파싱합니다.
    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]

    return (
        f"{city_name}: "
        f"{temperature}{units['temperature_2m']}, "
        f"풍속 {wind_speed}{units['wind_speed_10m']}"
    )


def print_raw_weather_data(data: dict[str, Any]) -> None:
    """도시별 원본 API 응답을 보기 좋게 출력합니다."""

    city_name = data["city_name"]
    print(f"\n[ASYNC] {city_name} 원본 API 응답(JSON -> Python dict)")

    # 원본 응답을 먼저 확인하면 어떤 key를 사용해야 하는지 알 수 있습니다.
    # 비동기 예제에서도 파싱 전 원본 구조를 확인하는 습관이 중요합니다.
    print(json.dumps(data, ensure_ascii=False, indent=2))
    print()


async def main() -> None:
    """여러 도시 날씨 요청을 동시에 실행합니다."""

    print_step("0. async main 함수가 시작되었습니다.")

    # AsyncClient는 비동기 HTTP 요청을 보내기 위한 httpx의 클라이언트입니다.
    # async with를 사용하면 요청이 끝난 뒤 연결 자원이 자동으로 정리됩니다.
    async with httpx.AsyncClient(timeout=10.0) as client:
        print_step("1. AsyncClient를 만들었습니다.")

        # 각 도시별 비동기 작업을 리스트로 만듭니다.
        # 이 시점의 tasks는 "실행할 수 있는 coroutine 목록"입니다.
        # 아직 모든 API 요청 결과가 준비된 상태는 아닙니다.
        tasks = [fetch_weather(client, city) for city in CITIES]
        print_step("2. 도시별 coroutine을 만들었습니다. 아직 실제 API 요청이 끝난 것은 아닙니다.")

        # asyncio.gather는 여러 coroutine을 동시에 실행하고 결과를 순서대로 모읍니다.
        # return_exceptions=True를 사용하면 한 도시 요청이 실패해도 전체 프로그램이 바로 중단되지 않습니다.
        # 실패한 결과는 Exception 객체로 results 리스트에 들어갑니다.
        print_step("3. asyncio.gather를 await합니다. 이제 여러 도시 요청이 동시에 진행됩니다.")
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print_step("4. 모든 도시 요청이 끝났습니다.")

    print_step("5. 원본 API 응답을 먼저 출력합니다.")
    for result in results:
        if isinstance(result, Exception):
            # result가 Exception이면 해당 도시 요청은 실패한 것입니다.
            print(f"날씨 API 호출 중 오류가 발생했습니다: {result}")
        else:
            # 정상 결과는 dict이므로 원본 JSON 구조를 출력할 수 있습니다.
            print_raw_weather_data(result)

    print_step("6. 원본 응답에서 필요한 값만 파싱해서 요약을 출력합니다.")
    for result in results:
        if isinstance(result, Exception):
            # 실패한 요청은 요약을 만들 수 없으므로 건너뜁니다.
            continue
        else:
            print(format_weather_summary(result))

    print_step("7. async main 함수가 끝났습니다.")


# Python 파일을 직접 실행했을 때만 main()을 실행합니다.
# asyncio.run은 async 함수가 실행될 수 있도록 이벤트 루프를 만들어 줍니다.
if __name__ == "__main__":
    print_step("프로그램 시작. asyncio.run이 이벤트 루프를 만들고 main을 실행합니다.")
    asyncio.run(main())
    print_step("프로그램 종료.")

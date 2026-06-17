"""Open-Meteo 날씨 API를 동기 방식으로 호출하는 예제입니다.

이 예제는 로그인이나 API key 없이 사용할 수 있는 Open-Meteo API를 사용합니다.
동기 방식은 요청을 보내고 응답을 받을 때까지 다음 코드로 넘어가지 않는 방식입니다.
"""

import json
from typing import Any

import httpx


# Open-Meteo의 날씨 조회 API 주소입니다.
# URL은 "어느 서버의 어떤 기능을 호출할지"를 나타냅니다.
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def print_step(message: str) -> None:
    """실행 흐름을 눈으로 확인하기 위해 단계 메시지를 출력합니다."""

    # API 호출은 눈에 보이지 않기 때문에, 단계별 로그를 출력하면
    # 어느 지점에서 기다리는지, 어느 지점에서 응답을 받았는지 확인할 수 있습니다.
    print(f"[SYNC] {message}")


def fetch_seoul_weather() -> dict[str, Any]:
    """서울의 현재 날씨 데이터를 Open-Meteo API에서 가져옵니다.

    반환값은 Python dict입니다. 외부 API의 JSON 응답은 httpx의
    response.json()을 통해 dict/list 구조로 바꿀 수 있습니다.
    """

    print_step("1. fetch_seoul_weather 함수에 들어왔습니다.")

    # params는 URL 뒤에 붙는 query string 값을 dict로 표현한 것입니다.
    # 예: ?latitude=37.5665&longitude=126.9780 같은 값이 자동으로 만들어집니다.
    params = {
        "latitude": 37.5665,  # 서울 위도입니다. API는 도시명이 아니라 좌표를 받습니다.
        "longitude": 126.9780,  # 서울 경도입니다.
        "current": "temperature_2m,wind_speed_10m",  # 현재 기온과 풍속만 요청합니다.
        "timezone": "Asia/Seoul",  # 응답 시간대를 한국 시간으로 맞춥니다.
    }

    print_step("2. 요청 파라미터를 만들었습니다.")
    print_step("3. httpx.get을 실행합니다. 동기 방식이라 응답이 올 때까지 여기서 기다립니다.")

    # timeout은 외부 API가 너무 오래 응답하지 않을 때 프로그램이 멈춰 보이는 것을 막습니다.
    # httpx.get은 요청을 보낸 뒤 응답이 도착할 때까지 현재 흐름을 기다리게 합니다.
    # 그래서 이 예제를 "동기 방식"이라고 부릅니다.
    response = httpx.get(OPEN_METEO_URL, params=params, timeout=10.0)

    print_step("4. API 응답을 받았습니다. 이제 다음 줄로 넘어갑니다.")

    # HTTP 상태 코드가 4xx/5xx이면 예외를 발생시킵니다.
    # 예: 주소가 틀렸거나, 서버 오류가 발생한 경우입니다.
    print_step("5. HTTP 상태 코드에 오류가 있는지 확인합니다.")
    response.raise_for_status()

    print_step("6. JSON 응답을 Python dict로 바꿔서 반환합니다.")

    # response.json()은 JSON 문자열을 Python의 dict/list 구조로 변환합니다.
    # 이후에는 data["current"]처럼 key를 이용해 필요한 값을 꺼낼 수 있습니다.
    return response.json()


def format_weather_summary(data: dict[str, Any]) -> str:
    """API 응답에서 필요한 값만 꺼내 초보자가 읽기 쉬운 문장으로 바꿉니다."""

    print_step("7. API 응답에서 필요한 값만 꺼내 출력 문장을 만듭니다.")

    # Open-Meteo 응답에서 current는 실제 현재 날씨 값이 들어 있는 영역입니다.
    current = data["current"]

    # current_units는 각 값의 단위가 들어 있는 영역입니다.
    # 예: temperature_2m의 단위는 "°C"입니다.
    units = data["current_units"]

    # 중첩 dict에서 필요한 값을 하나씩 꺼냅니다.
    # 원본 데이터를 먼저 출력해 보면 아래 key들이 어디에 있는지 확인할 수 있습니다.
    temperature = current["temperature_2m"]
    temperature_unit = units["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    wind_speed_unit = units["wind_speed_10m"]
    measured_at = current["time"]

    return (
        f"서울 현재 날씨({measured_at})\n"
        f"- 기온: {temperature}{temperature_unit}\n"
        f"- 풍속: {wind_speed}{wind_speed_unit}"
    )


def print_raw_weather_data(data: dict[str, Any]) -> None:
    """API가 돌려준 원본 JSON 구조를 보기 좋게 출력합니다.

    외부 API를 사용할 때는 먼저 원본 응답을 확인해야 합니다.
    그래야 어떤 key를 꺼내야 하는지, 중첩 구조가 어떻게 생겼는지 알 수 있습니다.
    """

    print("\n[SYNC] 원본 API 응답(JSON -> Python dict)")

    # json.dumps는 dict를 보기 좋은 JSON 문자열로 바꿔 줍니다.
    # ensure_ascii=False는 한글이 \uC11C 같은 코드로 깨져 보이지 않게 합니다.
    # indent=2는 들여쓰기를 넣어 중첩 구조를 읽기 쉽게 만듭니다.
    print(json.dumps(data, ensure_ascii=False, indent=2))
    print()


print_step("0. 프로그램을 시작합니다.")

try:
    # 외부 API 호출은 네트워크 상태, 서버 상태, 주소 오류 등으로 실패할 수 있습니다.
    # 그래서 try/except로 실패 상황을 함께 처리합니다.
    weather_data = fetch_seoul_weather()
except httpx.HTTPError as error:
    # 네트워크 오류, timeout, HTTP 오류는 실제 서비스에서 자주 발생할 수 있습니다.
    # 그래서 외부 API 호출 코드는 항상 실패 상황을 생각하고 작성해야 합니다.
    print(f"날씨 API 호출에 실패했습니다: {error}")
else:
    # try 블록에서 오류가 발생하지 않았을 때만 else 블록이 실행됩니다.
    print_raw_weather_data(weather_data)
    summary = format_weather_summary(weather_data)
    print_step("8. 날씨 요약을 화면에 출력합니다.")
    print(summary)
    print_step("9. 프로그램이 끝났습니다.")

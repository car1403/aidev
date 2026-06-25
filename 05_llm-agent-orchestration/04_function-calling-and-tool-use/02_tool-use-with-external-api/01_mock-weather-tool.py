"""외부 API 대신 Mock 데이터를 사용하는 도구 예제입니다."""

import json


WEATHER_DATA = {
    "seoul": {"temperature": 24, "condition": "맑음"},
    "busan": {"temperature": 22, "condition": "흐림"},
    "jeju": {"temperature": 25, "condition": "바람"},
}


def get_mock_weather(city: str) -> str:
    """도시 이름으로 Mock 날씨 정보를 반환합니다."""
    weather = WEATHER_DATA.get(city.lower())
    if weather is None:
        return json.dumps({"error": "지원하지 않는 도시입니다."}, ensure_ascii=False)
    return json.dumps({"city": city, **weather}, ensure_ascii=False)


print(get_mock_weather("Seoul"))
print(get_mock_weather("Jeju"))
print(get_mock_weather("Paris"))

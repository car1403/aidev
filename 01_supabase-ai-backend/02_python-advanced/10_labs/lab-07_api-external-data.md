# Lab 07. API 응답 처리

딕셔너리로 된 API 응답에서 필요한 필드만 추출해 요약 문자열을 만듭니다.

## 기본 실습

아래와 같은 API 응답이 있다고 가정합니다.

```python
response = {
    "user": {
        "name": "Mina",
        "email": "mina@example.com",
    },
    "stats": {
        "login_count": 5,
        "last_login": "2026-06-22",
    },
}
```

요구사항:

```text
1. 사용자 이름을 꺼냅니다.
2. 이메일을 꺼냅니다.
3. 로그인 횟수를 꺼냅니다.
4. "Mina님은 지금까지 5번 로그인했습니다." 형태의 문장을 만듭니다.
```

## 추가 실습. 로그인 없는 날씨 API 호출

외부 API를 호출하기 전에 먼저 동기/비동기 흐름만 확인합니다.

```powershell
python .\02_python-advanced\07_api-external-data\02_sync_flow_without_api.py
python .\02_python-advanced\07_api-external-data\03_async_flow_without_api.py
```

두 파일을 실행한 뒤 총 실행 시간이 어떻게 다른지 비교합니다.

그 다음 `07_api-external-data`의 날씨 API 예제를 실행해 봅니다.

```powershell
python .\02_python-advanced\07_api-external-data\04_weather_api_sync.py
python .\02_python-advanced\07_api-external-data\05_weather_api_async.py
```

## 확인 질문

1. Open-Meteo API를 사용할 때 API key가 필요한가요?
2. `response.json()`은 HTTP 응답을 어떤 Python 자료형으로 바꾸나요?
3. `timeout=10.0`을 설정하는 이유는 무엇인가요?
4. `async def` 함수와 일반 `def` 함수는 무엇이 다른가요?
5. `await`는 코드를 멈추는 것처럼 보이지만, 왜 비동기 처리에 도움이 되나요?
6. 여러 도시 날씨를 가져올 때 `asyncio.gather`를 사용하면 어떤 장점이 있나요?
7. `time.sleep`과 `asyncio.sleep`은 실행 흐름에서 어떤 차이가 있나요?

## 도전 과제

`05_weather_api_async.py`에 도시를 하나 더 추가해 봅니다.

예시:

```python
{"name": "대구", "latitude": 35.8714, "longitude": 128.6014}
```

도시를 추가한 뒤 실행 결과에 새 도시의 날씨가 함께 출력되는지 확인합니다.

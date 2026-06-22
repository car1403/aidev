# 07_api-external-data

HTTP API와 외부 데이터 처리 기초를 학습합니다.

처음에는 네트워크 없이 실행되는 mock 응답으로 API 응답 구조를 이해하고, 이후 로그인이나 API key가 필요 없는 Open-Meteo 날씨 API를 호출해 실제 외부 데이터를 가져옵니다.

Open-Meteo는 회원가입 없이 사용할 수 있는 날씨 API입니다. 이 단원에서는 서울의 현재 기온과 풍속을 가져오고, `async/await`를 사용해 여러 도시의 날씨를 동시에 요청하는 예제를 다룹니다.

## 이 단원에서 배우는 것

```text
API 응답은 보통 JSON 형태로 온다.
JSON은 Python에서 dict/list로 다룰 수 있다.
외부 API 호출은 실패할 수 있으므로 timeout과 예외 처리가 필요하다.
async/await는 시간이 오래 걸리는 I/O 작업을 기다리는 동안 다른 작업을 진행할 수 있게 한다.
여러 API를 동시에 호출할 때는 asyncio.gather를 사용할 수 있다.
```

## 예제 파일

| 파일 | 내용 |
| --- | --- |
| `01_api_response_processing.py` | 네트워크 없이 mock API 응답을 처리하는 기본 예제 |
| `02_sync_flow_without_api.py` | 외부 API 없이 `time.sleep`으로 동기 흐름만 이해하는 예제 |
| `03_async_flow_without_api.py` | 외부 API 없이 `asyncio.sleep`으로 비동기 흐름만 이해하는 예제 |
| `04_weather_api_sync.py` | Open-Meteo 날씨 API를 동기 방식으로 호출하는 예제 |
| `05_weather_api_async.py` | `async/await`로 여러 도시 날씨 API를 동시에 호출하는 예제 |

## 실행

```powershell
python .\02_python-advanced\07_api-external-data\01_api_response_processing.py
python .\02_python-advanced\07_api-external-data\02_sync_flow_without_api.py
python .\02_python-advanced\07_api-external-data\03_async_flow_without_api.py
python .\02_python-advanced\07_api-external-data\04_weather_api_sync.py
python .\02_python-advanced\07_api-external-data\05_weather_api_async.py
```

## 동기와 비동기 차이

두 예제는 일부러 실행 단계를 `print`로 보여줍니다. 출력 메시지의 순서를 보면 프로그램이 어디서 기다리고, 어디서 다른 요청으로 넘어가는지 알 수 있습니다.

외부 API를 호출하기 전에 먼저 아래 두 파일을 실행하면 동기와 비동기 흐름만 따로 볼 수 있습니다.

```text
02_sync_flow_without_api.py
03_async_flow_without_api.py
```

두 예제는 모두 커피 주문 3개를 처리하는 상황을 흉내 냅니다.

```text
동기 예제:
아메리카노 2초
-> 라떼 2초
-> 모카 2초
-> 총 약 6초

비동기 예제:
아메리카노, 라떼, 모카를 거의 동시에 시작
-> 각각 2초 기다림
-> 총 약 2초
```

동기 방식은 한 작업이 끝날 때까지 다음 줄로 넘어가지 않습니다.

```text
서울 날씨 요청
-> 응답을 받을 때까지 기다림
-> 결과 출력
```

`04_weather_api_sync.py`를 실행하면 `httpx.get`을 실행한 뒤 응답이 올 때까지 다음 단계 출력이 나오지 않습니다.
또한 API가 돌려준 원본 JSON을 먼저 출력한 뒤, 그중 `current`, `current_units`에서 필요한 값만 꺼내 요약 문장으로 바꾸는 과정을 확인합니다.

비동기 방식은 오래 걸리는 네트워크 요청을 기다리는 동안 다른 요청도 함께 시작할 수 있습니다.

```text
서울 날씨 요청 시작
부산 날씨 요청 시작
제주 날씨 요청 시작
-> 응답이 도착하는 대로 결과를 모음
```

`05_weather_api_async.py`를 실행하면 서울, 부산, 제주 요청이 각각 `await client.get` 지점에서 기다리지만, 이벤트 루프가 다른 도시 요청도 함께 진행시키는 것을 출력 순서로 확인할 수 있습니다.
비동기 예제도 도시별 원본 JSON을 먼저 보여준 뒤, 필요한 필드만 파싱해서 최종 요약을 출력합니다.

## 원본 데이터와 파싱

외부 API를 처음 사용할 때는 바로 필요한 값만 꺼내려고 하지 말고, 원본 응답을 먼저 확인하는 것이 좋습니다.

```text
1. 원본 JSON 응답을 본다.
2. 어떤 key가 있는지 확인한다.
3. 필요한 key만 꺼낸다.
4. 화면에 보여줄 문장이나 표 형태로 바꾼다.
```

예를 들어 Open-Meteo 응답에서는 현재 날씨가 아래 구조에 들어 있습니다.

```text
data["current"]["temperature_2m"]
data["current"]["wind_speed_10m"]
data["current_units"]["temperature_2m"]
data["current_units"]["wind_speed_10m"]
```

FastAPI, LLM API, Supabase API처럼 외부 서비스와 자주 통신하는 백엔드에서는 비동기 처리 개념을 이해하는 것이 중요합니다.

## API 출처

이 예제는 Open-Meteo Forecast API를 사용합니다.

```text
https://api.open-meteo.com/v1/forecast
```

수업용 예제에서는 API key 없이 사용할 수 있는 공개 API만 사용합니다.

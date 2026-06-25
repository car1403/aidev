# 05_comprehension-iterator

이 단원에서는 컴프리헨션과 제너레이터를 본 과정에서 필요한 만큼만 다룹니다.

핵심은 API 응답이나 Supabase 조회 결과처럼 `list[dict]` 형태의 데이터를 빠르게 필터링하고 변환하는 것입니다. 제너레이터는 이후 실시간 응답 스트리밍을 이해하기 위한 맛보기 정도로만 다룹니다.

## 이 단원에서 배우는 것

| 예제 | 핵심 내용 | 과정 연결 |
| --- | --- | --- |
| 01_list_comprehension_filter.py | 리스트 컴프리헨션으로 필터링/변환 | API 응답 목록 정리 |
| 02_dict_comprehension_lookup.py | 딕셔너리 컴프리헨션으로 조회용 구조 만들기 | id 기반 데이터 조회 |
| 03_api_response_transform.py | 중첩된 API 응답에서 필요한 값만 추출 | 외부 API, Supabase 응답 처리 |
| 04_generator_streaming_preview.py | `yield`로 값을 하나씩 생성 | SSE/스트리밍 응답 이해 준비 |

## 실행 전 준비

이 폴더에서는 별도의 `.venv`를 만들지 않습니다. `02_supabase-ai-backend` 최상위에서 만든 공통 가상환경을 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

## 실행 방법

```powershell
python .\02_python-advanced\05_comprehension-iterator\01_list_comprehension_filter.py
python .\02_python-advanced\05_comprehension-iterator\02_dict_comprehension_lookup.py
python .\02_python-advanced\05_comprehension-iterator\03_api_response_transform.py
python .\02_python-advanced\05_comprehension-iterator\04_generator_streaming_preview.py
```

## 핵심 확인

```text
list comprehension:
  기존 리스트를 새로운 리스트로 바꿀 때 사용합니다.

dict comprehension:
  리스트 데이터를 조회하기 쉬운 딕셔너리로 바꿀 때 사용합니다.

yield:
  값을 한 번에 모두 반환하지 않고 하나씩 생성할 때 사용합니다.
```

이번 단원에서는 복잡한 이터레이터 이론을 깊게 다루지 않습니다. 데이터 목록을 읽고, 필요한 것만 고르고, 화면/API 응답에 맞게 바꾸는 실습에 집중합니다.

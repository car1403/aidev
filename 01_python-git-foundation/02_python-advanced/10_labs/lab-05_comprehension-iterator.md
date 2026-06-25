# Lab 05. 컴프리헨션과 이터레이터

이 실습에서는 API 응답이나 Supabase 조회 결과처럼 여러 데이터가 들어 있는 목록을 짧고 명확하게 처리하는 방법을 연습합니다.

## 실습 목표

```text
1. list comprehension으로 필요한 데이터만 추출할 수 있습니다.
2. dict comprehension으로 id 기반 조회 구조를 만들 수 있습니다.
3. API 응답 형태의 dict/list 데이터를 화면 출력용 데이터로 바꿀 수 있습니다.
4. yield가 값을 하나씩 내보내는 흐름이라는 것을 이해할 수 있습니다.
```

## 실습 1. 활성 사용자만 추출하기

아래 사용자 목록에서 `active`가 `True`인 사용자 이름만 추출합니다.

```python
users = [
    {"id": 1, "name": "Mina", "active": True},
    {"id": 2, "name": "Jin", "active": False},
    {"id": 3, "name": "Seo", "active": True},
]

active_names = [user["name"] for user in users if user["active"]]

print(active_names)
```

확인할 내용:

```text
조건문을 comprehension 안에 넣을 수 있나요?
결과가 ["Mina", "Seo"] 형태로 나오나요?
```

## 실습 2. id로 바로 찾는 dict 만들기

사용자 목록을 `id` 기준으로 바로 찾을 수 있는 dict로 바꿉니다.

```python
users_by_id = {user["id"]: user for user in users}

print(users_by_id[1])
```

확인할 내용:

```text
리스트에서 매번 반복문으로 찾는 방식과 무엇이 다른가요?
Supabase에서 가져온 목록을 화면에서 빠르게 찾을 때 어떻게 활용할 수 있나요?
```

## 실습 3. API 응답 목록 변환하기

아래 API 응답에서 화면에 보여줄 데이터만 추출합니다.

```python
api_response = {
    "items": [
        {"question": "FastAPI란?", "answer": "Python 웹 API 프레임워크입니다.", "tokens": 120},
        {"question": "Supabase란?", "answer": "백엔드 기능을 제공하는 서비스입니다.", "tokens": 150},
    ]
}
```

요구사항:

```text
1. api_response["items"]에서 목록을 꺼냅니다.
2. question과 answer만 가진 새 dict 목록을 만듭니다.
3. tokens 값은 화면 출력용 데이터에서 제외합니다.
```

예시 결과:

```python
[
    {"question": "FastAPI란?", "answer": "Python 웹 API 프레임워크입니다."},
    {"question": "Supabase란?", "answer": "백엔드 기능을 제공하는 서비스입니다."},
]
```

## 실습 4. yield 흐름 이해하기

아래 함수는 한 번에 전체 문장을 반환하지 않고, 단어를 하나씩 내보냅니다.

```python
def stream_words(sentence: str):
    for word in sentence.split():
        yield word


for word in stream_words("AI 응답을 조금씩 표시합니다"):
    print(word)
```

확인할 내용:

```text
yield는 return과 어떻게 다른가요?
이 흐름이 이후 SSE 응답 스트리밍과 어떻게 연결될까요?
```

## 제출 기준

```text
1. list comprehension 예제가 있어야 합니다.
2. dict comprehension 예제가 있어야 합니다.
3. API 응답 dict/list를 화면 출력용 데이터로 변환해야 합니다.
4. yield 예제를 실행하고 출력 순서를 확인해야 합니다.
5. README 또는 메모 파일에 comprehension이 필요한 이유를 한 줄로 정리합니다.
```

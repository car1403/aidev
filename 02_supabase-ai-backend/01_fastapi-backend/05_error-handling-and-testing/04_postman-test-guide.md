# Postman 테스트

Postman은 API를 브라우저보다 자세히 테스트할 수 있는 도구입니다. 설치되어 있지 않다면 아래 순서로 준비합니다.

## Postman 설치

1. 브라우저에서 Postman 공식 다운로드 페이지를 엽니다.

```text
https://www.postman.com/downloads/
```

2. Windows용 설치 파일을 내려받아 실행합니다.
3. 설치가 끝나면 Postman을 실행합니다.
4. 로그인 화면이 나오면 계정으로 로그인하거나, 가능한 경우 가벼운 테스트용으로 계속 진행합니다.
5. 새 요청을 만들고 Method, URL, Body를 입력해 FastAPI API를 테스트합니다.

Postman 설치가 어렵다면 이 단원에서는 Swagger UI(`/docs`)와 PowerShell `Invoke-RestMethod`로도 같은 API 흐름을 확인할 수 있습니다.

## GET 요청

```text
GET http://127.0.0.1:8000/users/1
```

## POST 요청

```text
POST http://127.0.0.1:8000/items
```

Body는 `raw`와 `JSON`을 선택합니다.

```json
{
 "name": "Keyboard",
 "price": 30000
}
```


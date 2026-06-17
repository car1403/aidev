# 05 API Supabase Flow

미니 프로젝트에서 데이터가 이동하는 흐름을 설명합니다.

## 데이터 등록 흐름

```text
사용자가 Streamlit에서 입력
-> Streamlit이 FastAPI POST API 호출
-> FastAPI가 입력값 검증
-> FastAPI가 Supabase 테이블에 저장
-> FastAPI가 저장 결과를 JSON으로 반환
-> Streamlit이 결과 메시지 표시
```

## 데이터 조회 흐름

```text
사용자가 조회 버튼 클릭
-> Streamlit이 FastAPI GET API 호출
-> FastAPI가 Supabase 테이블에서 데이터 조회
-> FastAPI가 JSON 목록 반환
-> Streamlit이 표 또는 채팅 UI로 표시
```

## FastAPI가 하는 일

- 요청을 받습니다.
- 데이터 형식을 확인합니다.
- Supabase에 저장하거나 조회합니다.
- AI API 호출이 필요한 경우 서버 쪽에서 처리합니다.
- JSON으로 응답합니다.

## Streamlit이 하는 일

- 화면을 보여줍니다.
- 사용자의 입력을 받습니다.
- 버튼 클릭 시 API를 호출합니다.
- 응답을 표, 메시지, 채팅 UI로 보여줍니다.

## Supabase가 하는 일

- 데이터를 저장합니다.
- Auth를 사용하면 사용자 인증을 담당합니다.
- RLS 정책으로 사용자별 데이터 접근을 제어합니다.
- Table Editor와 SQL Editor로 테이블을 관리합니다.

## 기억할 문장

```text
Streamlit은 화면, FastAPI는 처리, Supabase는 저장과 권한 관리를 담당합니다.
```

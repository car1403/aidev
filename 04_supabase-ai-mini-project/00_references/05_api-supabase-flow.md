# 05 API Supabase Flow

이 문서는 04 미니 프로젝트에서 데이터가 이동하는 흐름을 설명합니다.

04 과정의 기본 구조는 다음과 같습니다.

```text
Streamlit
-> FastAPI
-> Supabase
```

## 데이터 등록 흐름

사용자가 화면에서 로그나 질문을 입력하면 아래 순서로 처리됩니다.

```text
1. 사용자가 Streamlit 화면에서 입력한다.
2. Streamlit이 FastAPI POST API를 호출한다.
3. FastAPI가 입력값을 Pydantic 모델로 검증한다.
4. FastAPI가 Supabase 테이블에 데이터를 저장한다.
5. FastAPI가 저장 결과를 JSON으로 반환한다.
6. Streamlit이 성공 또는 실패 메시지를 화면에 표시한다.
```

팀 프로젝트에서는 보통 `service_logs`, `messages`, `feedbacks` 테이블에 데이터를 저장합니다.

## 데이터 조회 흐름

사용자가 조회 버튼을 누르거나 화면이 새로고침되면 아래 순서로 처리됩니다.

```text
1. 사용자가 Streamlit 화면에서 조회 버튼을 누른다.
2. Streamlit이 FastAPI GET API를 호출한다.
3. FastAPI가 Supabase 테이블에서 데이터를 조회한다.
4. FastAPI가 JSON 목록을 반환한다.
5. Streamlit이 표, 차트, 카드, 채팅 UI로 데이터를 표시한다.
```

## FastAPI가 하는 일

- 요청을 받습니다.
- 입력 데이터 형식을 확인합니다.
- Supabase에 저장하거나 조회합니다.
- Gemini API 호출이 필요한 경우 서버 쪽에서 처리합니다.
- 오류가 발생하면 표준화된 에러 응답을 반환합니다.
- JSON 또는 SSE 스트리밍 응답을 반환합니다.

## Streamlit이 하는 일

- 화면을 보여줍니다.
- 사용자 입력을 받습니다.
- 버튼 클릭 시 FastAPI API를 호출합니다.
- 응답을 표, 차트, 메시지, 채팅 UI로 보여줍니다.
- 로딩 상태와 오류 메시지를 표시합니다.

## Supabase가 하는 일

- 데이터를 저장합니다.
- Auth를 사용할 경우 사용자 인증을 담당합니다.
- RLS 정책으로 사용자별 데이터 접근을 제어합니다.
- Table Editor와 SQL Editor로 테이블을 관리합니다.

## SSE 응답 흐름

SSE는 AI 응답을 한 번에 받는 것이 아니라 작은 조각으로 나누어 실시간 표시하는 방식입니다.

```text
1. Streamlit이 FastAPI SSE 엔드포인트를 호출한다.
2. FastAPI가 Gemini 응답을 chunk 단위로 보낸다.
3. Streamlit이 받은 chunk를 화면에 누적 표시한다.
4. 응답이 끝나면 최종 메시지와 실행 로그를 Supabase에 저장한다.
```

## 기억할 문장

```text
Streamlit은 화면, FastAPI는 처리, Supabase는 저장과 권한 관리를 담당합니다.
```

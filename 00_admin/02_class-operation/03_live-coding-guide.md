# 03. Live Coding Guide

수업 중 실시간 코딩을 진행할 때의 기준입니다.

## 라이브 코딩 원칙

```text
1. 한 번에 많은 코드를 작성하지 않는다.
2. 파일을 만들기 전에 왜 필요한지 설명한다.
3. 함수 하나를 만들면 바로 실행해 확인한다.
4. 오류가 나면 숨기지 않고 같이 읽는다.
5. 완성보다 이해를 우선한다.
```

## 추천 진행 방식

```text
1. 빈 파일 또는 템플릿 파일을 연다.
2. import를 작성한다.
3. 가장 작은 함수 하나를 작성한다.
4. 실행한다.
5. 출력 결과를 확인한다.
6. 다음 기능을 붙인다.
```

## FastAPI 라이브 코딩 예

```text
1. app = FastAPI() 작성
2. /health 엔드포인트 작성
3. uvicorn 실행
4. /docs 확인
5. Pydantic 모델 추가
6. POST API 추가
7. Supabase 저장 연결
```

## Streamlit 라이브 코딩 예

```text
1. st.title 작성
2. st.text_input 작성
3. 버튼 클릭 처리
4. httpx로 API 호출
5. 응답을 st.json 또는 st.write로 표시
6. session_state로 상태 유지
```

## SSE 라이브 코딩 예

```text
1. 일반 /api/chat API 먼저 작성
2. StreamingResponse 개념 설명
3. /api/chat/stream 작성
4. chunk가 하나씩 전송되는지 확인
5. Streamlit에서 httpx.stream으로 읽기
6. st.empty로 화면 누적 표시
7. 최종 응답 저장 흐름 설명
```

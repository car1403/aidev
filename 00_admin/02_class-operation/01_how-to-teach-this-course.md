# 01. How To Teach This Course

이 과정은 초보자가 AI 서비스를 단계적으로 이해하도록 구성되어 있습니다.

## 강의 기본 방식

```text
개념 설명
-> 폴더 구조 확인
-> README Preview로 읽기
-> 시연
-> 실습
-> 오류 해결
-> 체크리스트 확인
```

## 설명할 때의 기준

수업 참여자에게 기술 용어를 먼저 던지기보다, 역할을 먼저 설명합니다.

예:

```text
FastAPI:
화면에서 보낸 요청을 받아 처리하는 서버

Streamlit:
사용자가 보는 화면

Supabase:
데이터를 저장하는 곳

SSE:
AI 응답을 실시간으로 조금씩 화면에 보내는 방식

Docker:
실행 환경을 컨테이너로 묶어 관리하는 도구
```

## 초보자가 어려워하는 지점

```text
현재 폴더 위치
.venv 활성화
requirements.txt 설치
.env와 .env.example 차이
FastAPI 서버와 Streamlit 서버를 각각 실행하는 방식
API_BASE_URL 포트 번호
Supabase key 종류
Docker를 언제 쓰고 언제 안 쓰는지
```

## 반복 안내 문장

수업 중 아래 문장을 계속 반복하면 좋습니다.

```text
지금 내 PowerShell 위치가 어디인지 먼저 확인합니다.
README를 Preview로 먼저 봅니다.
.venv가 켜져 있는지 확인합니다.
한 번에 많이 하지 말고 한 단계씩 실행합니다.
오류 메시지는 적이 아니라 힌트입니다.
```

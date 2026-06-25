# 02 Role Assignment

역할 분담은 팀 프로젝트의 속도를 결정합니다.

역할은 사람을 고정된 직무로 나누기 위한 것이 아니라, 어떤 작업을 누가 먼저 책임지고 정리할지 정하는 기준입니다.

## 권장 팀 구성

4~5명 기준으로 아래 역할을 권장합니다.

```text
Backend/API
-> FastAPI 엔드포인트, Pydantic 모델, 오류 응답, Supabase 연동

Database/Supabase
-> 테이블 설계, SQL 작성, RLS 검토, 테스트 데이터 준비

Frontend/UI
-> Streamlit 화면 구성, API 호출, 표와 차트, 상태 메시지

AI/Quality
-> Gemini 연동, 프롬프트, 응답 품질, 피드백 데이터 활용

Docs/Presentation
-> API 문서, 화면 설계서, DB 설계서, 발표 자료, 제출 체크리스트
```

## 작은 팀일 때

3명 이하라면 역할을 합쳐도 됩니다.

```text
Backend + Database
Frontend + Quality
Docs + Presentation
```

## 역할 분담 시 확인할 질문

- 누가 `.env`와 key 보안 기준을 관리하는가?
- 누가 Supabase 테이블 SQL을 최종 정리하는가?
- 누가 FastAPI 실행 방법을 README에 정리하는가?
- 누가 Streamlit 화면 흐름을 문서화하는가?
- 누가 발표용 시연 순서를 정하는가?

## 협업 기준

- 작업 시작 전 파일 이름과 담당자를 정합니다.
- 같은 파일을 동시에 크게 수정하지 않습니다.
- 하루가 끝나기 전에 README와 체크리스트를 갱신합니다.
- 실행이 되지 않는 코드는 바로 팀원에게 공유합니다.
- `.env` 파일과 실제 API key는 공유 저장소에 올리지 않습니다.

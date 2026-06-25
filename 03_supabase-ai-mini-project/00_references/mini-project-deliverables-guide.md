# Mini Project Deliverables Guide

이 문서는 `03_supabase-ai-mini-project`의 필수 산출물을 작성할 때 참고하는 가이드입니다.

산출물은 문서만 따로 만드는 것이 아니라, 실제 구현 결과와 서로 맞아야 합니다.

## 산출물 1. API 설계 문서

작성 파일:

```text
docs/api-spec.md
```

확인 질문:

- 엔드포인트 URL이 리소스 중심으로 일관되게 작성되었나요?
- `GET`, `POST`, `PUT`, `DELETE`가 의미에 맞게 사용되었나요?
- 요청 Body와 응답 Body 예시가 있나요?
- Pydantic Request/Response 모델이 문서와 코드에서 같은 구조인가요?
- 에러 응답에 HTTP Status Code, 에러 코드, 메시지, 상세 정보가 포함되나요?
- 4xx/5xx 예외 상황별 처리 규칙이 문서화되어 있나요?

## 산출물 2. 화면 설계서

작성 파일:

```text
docs/ui-design.md
```

확인 질문:

- 메인, 상세, 입력, 설정, 오류 화면이 정리되어 있나요?
- 와이어프레임 또는 화면 배치 설명이 있나요?
- 버튼, 입력폼, 테이블, 차트의 역할이 설명되어 있나요?
- 클릭, 새로고침, 필터, 저장 같은 사용자 액션에 대한 반응이 정의되어 있나요?
- 화면별 API 호출과 로딩/오류 표시 방식이 정리되어 있나요?

## 산출물 3. 데이터베이스 설계서

작성 파일:

```text
docs/supabase-schema.md
```

확인 질문:

- 필요한 테이블이 정리되어 있나요?
- `profiles`, `conversations`, `messages`, `service_logs`, `feedbacks` 중 어떤 테이블을 사용할지 정했나요?
- PK/FK 관계가 설명되어 있나요?
- 컬럼 이름, 타입, 기본값, 제약조건이 정리되어 있나요?
- RLS 적용 여부와 사용자별 접근 제어 기준이 설명되어 있나요?
- Supabase SQL Editor에서 실행할 SQL과 문서 내용이 일치하나요?

## 산출물 4. 대시보드 구현 결과물

작성 파일:

```text
docs/dashboard-result.md
frontend/app.py
```

확인 질문:

- 대시보드가 로컬 환경에서 실행되나요?
- 로그 수집, 조회, 시각화가 시연 가능한가요?
- 사용자 피드백이 저장되거나 지표에 반영되나요?
- AI 응답 품질 개선 방향이 문서화되어 있나요?
- SSE 또는 자동 새로고침 기반 실시간 표시 방식이 설명되어 있나요?
- 로컬 실행 URL이 문서에 정리되어 있나요?
- 무료 배포를 진행했다면 Render, Upstash, Streamlit Community Cloud URL이 정리되어 있나요?

## 제출 전 최종 확인

```text
1. README.md만 보고 실행할 수 있는가?
2. .env 파일이 제출되거나 GitHub에 올라가지 않았는가?
3. .env.example에는 실제 key가 없는가?
4. Supabase 테이블과 API 코드의 테이블 이름이 일치하는가?
5. 문서의 기능 목록과 실제 화면 기능이 일치하는가?
6. 배포는 선택 제출임을 명확히 표시했는가?
```

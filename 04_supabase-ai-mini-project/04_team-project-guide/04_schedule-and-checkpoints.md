# 04 Schedule and Checkpoints

3일 프로젝트 권장 일정입니다.

하루 8시간 진행을 기준으로 작성했습니다. 팀 속도에 따라 SSE, 배포, OpenAI 비교 호출은 선택 확장으로 조정합니다.

## Day 1

목표: 설계와 첫 실행 성공

- 실시간 로그 대시보드 주제 확정
- 팀 역할 분담
- `05_project-templates`에서 문서, SQL, 환경 변수, 체크리스트 템플릿 확인
- API 설계 문서 초안 작성
- 화면 설계서 초안 작성
- Supabase 테이블 설계 초안 작성
- `03_supabase-and-sse-practice/01_supabase-project-and-schema` 흐름 확인
- FastAPI 기본 API 구현
- Streamlit 기본 화면 구성

Day 1 종료 기준:

```text
백엔드 실행 성공
프론트엔드 실행 성공
Supabase 테이블 초안 완성
API 설계 문서 초안 작성
화면 설계서 초안 작성
DB 설계서 초안 작성
```

## Day 2

목표: 로그 저장, 조회, 시각화 구현

- 로그 생성 API 구현
- 로그 목록/상세 조회 API 구현
- Supabase CRUD 기능 확인
- `03_supabase-and-sse-practice/02_fastapi-supabase-api` 흐름 적용
- `03_supabase-and-sse-practice/03_streamlit-dashboard-ui` 흐름 적용
- 로그 테이블 또는 차트 표시
- 사용자 피드백 저장 또는 표시 기능 구현
- `03_supabase-and-sse-practice/04_service-log-and-feedback` 흐름 적용
- SSE 또는 새로고침 기반 실시간 표시 방식 선택

Day 2 종료 기준:

```text
데이터 생성 성공
데이터 조회 성공
Streamlit 화면에서 API 호출 성공
대시보드 기본 지표 표시 성공
```

## Day 3

목표: 최종 산출물 정리와 시연 준비

- 대시보드 화면 마무리
- API 설계 문서 보완
- 화면 설계서 보완
- 데이터베이스 스키마 설계서 보완
- 대시보드 구현 결과물 문서 작성
- SSE를 적용했다면 `03_supabase-and-sse-practice/05_sse-streaming-ai-response` 기준으로 문서 보완
- 테스트 체크리스트 작성
- 발표 자료 작성
- 최종 시연 리허설

Day 3 종료 기준:

```text
처음부터 실행 가능한가?
로그 수집/조회/시각화를 시연할 수 있는가?
필수 산출물 4종을 제출할 수 있는가?
팀원별 구현 내용을 설명할 수 있는가?
민감 정보가 화면/문서/저장소에 노출되지 않는가?
```

## 범위 축소 기준

시간이 부족하면 아래 순서로 범위를 줄입니다.

```text
1. 무료 배포 생략
2. SSE 구현 대신 streaming-response-design.md에 설계만 작성
3. AI 응답은 mock 또는 Gemini 단일 호출로 단순화
4. 차트 종류를 줄이고 테이블 핵심 지표 중심으로 구성
5. 로그인/Auth는 설계 문서에 반영하고 구현은 생략
```

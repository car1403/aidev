# 02 Project Architecture

이 문서는 `03_supabase-ai-mini-project`의 전체 구조를 설명합니다.

03 과정은 `01_supabase-ai-backend`와 `02_supabase-ai-frontend`에서 배운 내용을 연결해, Supabase 기반 미니 프로젝트를 만드는 과정입니다.

## 1. 전체 구조

```text
Streamlit Frontend
-> FastAPI Backend
-> Supabase Database/Auth
-> Gemini API
```

역할을 나누어 보면 다음과 같습니다.

| 구성 요소 | 역할 |
| --- | --- |
| Streamlit | 사용자가 보는 화면입니다. 입력, 버튼, 표, 차트, 대시보드를 담당합니다. |
| FastAPI | 프론트엔드 요청을 받아 Supabase와 Gemini API를 호출하는 백엔드 서버입니다. |
| Supabase | 사용자, 대화, 메시지, 서비스 로그, 피드백 데이터를 저장합니다. |
| Gemini API | 01~03 과정의 기본 AI 응답 생성 API입니다. |
| OpenAI API | 선택 비교 실습으로 유지합니다. 기본 흐름은 Gemini입니다. |

Docker, Docker Compose, 로컬 PostgreSQL 컨테이너, Redis 컨테이너는 03 과정의 기본 실행 방식이 아닙니다. 해당 내용은 `06_multi-agent-service-ops`에서 서비스 운영 관점으로 학습합니다.

## 2. Frontend

Streamlit은 사용자가 보는 화면입니다.

주요 역할:

```text
사용자 질문 또는 로그 입력
FastAPI API 호출
로그 목록과 대시보드 표시
AI 응답 표시
SSE 응답 chunk를 화면에 누적 표시
오류 메시지와 로딩 상태 표시
```

초보자는 Streamlit을 “Python으로 빠르게 만드는 웹 화면”으로 이해하면 됩니다.

## 3. Backend

FastAPI는 요청 검증과 API 응답을 담당합니다.

주요 역할:

```text
요청 데이터 검증
Supabase 테이블에 데이터 저장
Supabase 테이블에서 데이터 조회
Gemini API 호출
SSE 스트리밍 응답 생성
프론트엔드에 JSON 또는 스트리밍 응답 반환
```

API key는 가능하면 FastAPI 백엔드에서만 사용합니다. 화면 코드에 직접 key를 넣지 않는 것이 안전합니다.

## 4. Supabase

Supabase는 데이터 저장과 인증 기반을 담당합니다.

03 과정에서는 실습 단계에 따라 테이블을 구분합니다.

| 위치 | 테이블 | 용도 |
| --- | --- | --- |
| 입문 샘플 | `learning_logs` | Supabase 연결, 저장, 조회 감각 익히기 |
| 팀 프로젝트 | `profiles` | 사용자 프로필 |
| 팀 프로젝트 | `conversations` | 대화방 또는 세션 |
| 팀 프로젝트 | `messages` | 사용자/AI 메시지 |
| 팀 프로젝트 | `service_logs` | 서비스 실행 로그, 오류 로그, 요청 로그 |
| 팀 프로젝트 | `feedbacks` | 사용자 피드백과 AI 품질 개선 기록 |

최종 팀 프로젝트에서는 `service_logs`, `messages`, `feedbacks`를 중심으로 대시보드와 AI 응답 품질 개선 흐름을 구성합니다.

## 5. AI API

03 과정에서는 Gemini API를 기본 AI API로 사용합니다.

기본 모델 예시:

```env
GEMINI_MODEL=gemini-2.5-flash-lite
```

OpenAI API 예제는 삭제하지 않고 선택 비교 실습으로 유지합니다.

```env
OPENAI_MODEL=gpt-4.1-mini
```

수업 흐름은 다음 기준을 따릅니다.

```text
기본 구현: Gemini
비교/확장 실습: OpenAI
운영 배포 자동화: 06 과정에서 별도 학습
```

## 6. SSE 스트리밍 구조

SSE는 Server-Sent Events의 줄임말입니다. 서버가 응답을 한 번에 보내는 것이 아니라, 작은 조각(chunk)으로 계속 보내는 방식입니다.

03 과정에서는 다음 흐름으로 다룹니다.

```text
사용자 질문 입력
-> Streamlit이 FastAPI SSE 엔드포인트 호출
-> FastAPI가 AI 응답 chunk를 순서대로 전송
-> Streamlit이 화면에 응답을 누적 표시
-> 완료 후 최종 메시지와 로그를 Supabase에 저장
```

SSE는 실시간 화면 표시를 위한 통신 방식이고, Supabase는 최종 데이터 저장소입니다. 두 역할을 구분하면 이해하기 쉽습니다.

## 7. 로컬 실행 주소

03 과정에서는 FastAPI와 Streamlit을 로컬 PC에서 실행합니다.

```text
FastAPI: http://127.0.0.1:8000
Streamlit: http://127.0.0.1:8501
Supabase: Supabase Cloud 프로젝트 URL 사용
```

프론트엔드가 백엔드를 호출할 때는 보통 다음 주소를 사용합니다.

```env
API_BASE_URL=http://127.0.0.1:8000
```

## 8. 선택 배포 구조

03 과정의 배포는 필수가 아닙니다. 로컬에서 동작하는 것이 기본 제출 기준입니다.

시간이 충분하면 다음 무료 배포 흐름을 선택적으로 진행할 수 있습니다.

```text
Streamlit Community Cloud
-> Render FastAPI
-> Supabase Cloud
-> Upstash Redis 선택 사용
```

이 배포는 “운영 자동화”가 아니라 “완성한 프로젝트를 외부 URL로 시연하는 선택 실습”입니다.

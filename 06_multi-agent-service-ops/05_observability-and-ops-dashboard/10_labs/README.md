# 10 Labs

이 폴더는 로그, tracing, 운영 대시보드, 실행 상태 관리 실습을 정리합니다.

## Lab 목록

| Lab | 내용 |
| --- | --- |
| `lab-01_event-history-logging.md` | 이벤트 로그 기록 |
| `lab-02_trace-agent-execution.md` | Agent 실행 trace |
| `lab-03_ops-dashboard-streamlit.md` | Streamlit 운영 대시보드 |
| `lab-04_execution-status-management.md` | 실행 상태 관리 |
| `lab-05_langsmith-tracing-practice.md` | LangSmith식 추적 구조 이해 |

## 공통 기준

- request_id를 기준으로 로그를 묶습니다.
- 실패 단계와 복구 단계를 구분합니다.
- 대시보드에 보여줄 지표를 정리합니다.
